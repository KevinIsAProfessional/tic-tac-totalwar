import React from 'react';

class Square extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      owner: '-',
      isPlayerX: props.isPlayerX,
    }
    this.setOwner = this.setOwner.bind(this);
  }

  setOwner() {
    this.setState((state) => {
      if (this.state.isPlayerX) {
        return {owner: "X"}
      } else {
        return {owner: "O"}
      }
    });
  }

  render() {
    return (
      <button onClick={this.setOwner}>{this.state.owner}</button>
    )
  }
}

class Game extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isPlayerX: true,
    }
  }

  render() {
    return ( 
      <div>
        <div>
          <Square isPlayerX={this.state.isPlayerX} />
          <Square isPlayerX={this.state.isPlayerX} />
          <Square isPlayerX={this.state.isPlayerX} />

        </div>
        <div>
          <Square isPlayerX={this.state.isPlayerX} />
          <Square isPlayerX={this.state.isPlayerX} />
          <Square isPlayerX={this.state.isPlayerX} />
        </div>
        <div>
          <Square isPlayerX={this.state.isPlayerX} />
          <Square isPlayerX={this.state.isPlayerX} />
          <Square isPlayerX={this.state.isPlayerX} />
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

