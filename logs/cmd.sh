#conda activate arena
while true; do
    rm elo_results.pkl
    rm clean.json
    cp ../*-conv.json server0  #copy
    python3 ../fastchat/serve/monitor/clean_battle_data.py
    mv clean_battle*.json clean.json
    python3 ../fastchat/serve/monitor/elo_analysis.py --clean-battle-file clean.json
    mv elo_results*.pkl elo_results.pkl
    python3 hf_upload.py
    sleep 7200
done