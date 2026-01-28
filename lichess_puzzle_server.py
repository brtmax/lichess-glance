from flask import Flask, send_file, jsonify
import requests
import chess
import chess.pgn
from io import StringIO, BytesIO
import chess.svg

app = Flask(__name__)
LICHESS_PUZZLE_URL = "https://lichess.org/api/puzzle/daily"
HOST_IP = ""
PORT = 5000

@app.route("/daily_puzzle.png")
def daily_puzzle():
    resp = requests.get(LICHESS_PUZZLE_URL)
    data = resp.json()

    pgn_text = data["game"]["pgn"]
    initial_ply = data["puzzle"]["initialPly"]

    game = chess.pgn.read_game(StringIO(pgn_text))
    board = game.board()

    for i, move in enumerate(game.mainline_moves()):
        if i >= initial_ply:
            break
        board.push(move)

    svg_data = chess.svg.board(board=board)
    try:
        import cairosvg
        png_data = BytesIO(cairosvg.svg2png(bytestring=svg_data))
        png_data.seek(0)
        return send_file(png_data, mimetype="image/png")
    except ImportError:
        return "Install cairosvg to render PNG", 500

@app.route("/daily_puzzle.json")
def daily_puzzle_json():
    return jsonify({
        "url": f"http://{HOST_IP}:{PORT}/daily_puzzle.png",
        "title": "Lichess Daily Puzzle",
        "link": "https://lichess.org/training/daily"
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
