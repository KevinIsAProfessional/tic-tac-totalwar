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
    return <Square isPlayerX={this.state.isPlayerX} /> 
  } 
}

function App() {
  return (
    <Game />
  );
}

export default App;

