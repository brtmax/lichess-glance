# lichess-glance
Lichess daily puzzle widget for glance

The [Lichess API](https://lichess.org/api#tag/bot) provides the daily puzzle in pgn, and this is a small flask server which draws the board, converts it to a PNG and serves it. The [glance](https://github.com/glanceapp/glance) widget fetches it. 

There's a similar excellent [widget](https://github.com/glanceapp/community-widgets/blob/main/widgets/chess-puzzle/README.md) for Chess.com. 
