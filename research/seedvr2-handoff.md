# SeedVR2: unde am rămas (23 nov 2026)

**Scop:** să înlocuim amestecul actual (60% Real-ESRGAN + 40% Lanczos) pentru clipurile 480p ale lui Thomas cu SeedVR2-3B (ByteDance, Apache-2.0), care restaurează fața mai natural, fără aspectul „de ceară”.

## Ce s-a încercat

1. **Space-ul oficial `ByteDance-Seed/SeedVR2-3B`:** a picat după 3 s cu `RuntimeError`, fără cotă consumată. Cauza, aflată din codul portului `Upsampler/seedvr2-3b`, are două părți:
   - instalează `apex` compilat pentru Python 3.10, iar ZeroGPU rulează acum 3.12;
   - are trei funcții `@spaces.GPU(duration=100)` înlănțuite, deci o cerere rezervă 300 s.
2. **`Upsampler/seedvr2-3b`** repară ambele probleme, dar e doar pentru imagini, deci nu e bun pentru video (cadru cu cadru ar pâlpâi).
3. **Space propriu, construit fără cotă:** `<cont>/siphon-seedvr2-video`, privat, ZeroGPU, în stare **RUNNING**.
   - Codul e în `siphonfiles/siphon-ep002`, folderul `spaces/seedvr2-video/`:
     - `upstream/` = copia Upsampler;
     - `reference/` = `app.py` oficial;
     - `overlay/app.py` = partea de video readusă: max 121 de cadre, padding 4n+1, țintă 1920x1080 sau 1280x720, corecție de culoare wavelet, fps păstrat, un singur `@spaces.GPU`, plafon 240 s.
   - Workflow-uri:
     - `space-fetch.yml` aduce codul Upsampler;
     - `space-deploy.yml` publică Space-ul, folosind secretul `HF_WRITE_TOKEN`;
     - `seedvr2.yml` + `scripts/seedvr2_clip.py` rulează restaurarea, cu inputurile `clip`, `fps`, `space=own`, `target`.
4. **Primul test real** pe clipul de test `presenter/tests/thomas_k7_1_480p_4s.mp4` (k7_1 din ep. 001, 4 s, 120 de cadre la 25 fps), la 1920x1080, toate cadrele odată:
   - **încercarea 1** a picat local, din cauza formatului de intrare `gr.Video`; reparat cu `{"video": handle_file(...)}`;
   - **încercarea 2** a picat pe GPU după ~70 s cu `NVML_SUCCESS == r INTERNAL ASSERT FAILED`, adică lipsă de memorie. A consumat ~1 min de cotă și n-a produs niciun rezultat.

## Pasul următor

Doar cu acordul proprietarului, după resetarea cotei ZeroGPU:
1. Rerulare `seedvr2.yml` cu `target=1280x720` și/sau `chunk_frames=41`.
2. O planșă de comparație pe față, pe aceleași cadre: original Lanczos, Real-ESRGAN (`sr2` din `siphon-ep001`, branch `renders`, `kaggle/run-16`) și SeedVR2.
3. Notăm cota reală consumată.

## Reguli de păstrat

- Nicio rulare pe ZeroGPU sau Kaggle fără acordul proprietarului.
- Tot ce se produce intră în git.
- Totul e notat în `CLAUDE.md` din `siphon-ep002` (jurnal + secțiunea 8).
