import React from 'react';
import styled from 'styled-components';

const Button = styled.button`
  background: transparent;
  color: black;
  border-radius: 3px;
  border: 2px solid palevioletred;
  color: palevioletred;
  font-size: 20px;
  margin: .1em .1em;
  padding: .75em 1.25em;
`


class Square extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      row: this.props.row,
      col: this.props.col
    }
  }

  render() {
    return (
      <Button onClick={this.props.setOwner.bind(this, this.state.row, this.state.col)}>{this.props.owner}</Button>
    )
  }
}

class Game extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      activePlayer: 'X',
      gameBoard: [
        ["--","--","--"],
        ["--","--","--"],
        ["--","--","--"],
      ],
    }
    this.setOwner = this.setOwner.bind(this);
    this.checkForWinner = this.checkForWinner.bind(this);
  }

  checkForWinner(winner) {
    let win = false;
    let winningConfigs = [
      [[0,0],[0,1],[0,2]],
      [[1,0],[1,1],[1,2]],
      [[2,0],[2,1],[2,2]],
      [[0,0],[1,0],[2,0]],
      [[0,1],[1,1],[2,1]],
      [[0,2],[1,2],[2,2]],
      [[0,0],[1,1],[2,2]],
      [[0,2],[1,1],[2,0]],
    ]
    winningConfigs.map( (config) => {
      let line = []
      for (let set=0; set<3; set++) {
        let row = config[set][0];
        let col = config[set][1];
        line.push(this.state.gameBoard[row][col])
      }
      if (line[0] === winner){
        if (line[1] === winner) {
          if (line[2] === winner) {
            win = true
          }
        }
      }
    });
    return win;
  }

  setOwner(row, col) {
    if (this.state.gameBoard[row][col] === "X" || this.state.gameBoard[row][col] === "0") {
      return null
    };

    let swap = {'X':'0','0':'X'};
    let newBoard = this.state.gameBoard;
    newBoard[row][col] = this.state.activePlayer;
    this.setState({
      gameBoard: newBoard,
      activePlayer: swap[this.state.activePlayer],
    });

    if (this.checkForWinner(this.state.activePlayer)) {
      console.log("winner");
    } else {
      console.log("no winner");
    }

  }

  render() {
    return (
      <div>
        <div>Active Player: {this.state.activePlayer}</div>
        <div>
          <Square row={0} col={0} setOwner={this.setOwner} owner={this.state.gameBoard[0][0]} />
          <Square row={0} col={1} setOwner={this.setOwner} owner={this.state.gameBoard[0][1]} />
          <Square row={0} col={2} setOwner={this.setOwner} owner={this.state.gameBoard[0][2]} />
        </div>
        <div>
          <Square row={1} col={0} setOwner={this.setOwner} owner={this.state.gameBoard[1][0]} />
          <Square row={1} col={1} setOwner={this.setOwner} owner={this.state.gameBoard[1][1]} />
          <Square row={1} col={2} setOwner={this.setOwner} owner={this.state.gameBoard[1][2]} />
        </div>
        <div>
          <Square row={2} col={0} setOwner={this.setOwner} owner={this.state.gameBoard[2][0]} />
          <Square row={2} col={1} setOwner={this.setOwner} owner={this.state.gameBoard[2][1]} />
          <Square row={2} col={2} setOwner={this.setOwner} owner={this.state.gameBoard[2][2]} />
        </div>
        <div>
          <button>Reset</button>
          <button>Style</button>
        </div>
      </div>
    )
  }
}

function App() {
  return (
    <Game />
  );
}

export default App;

