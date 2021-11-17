import React, { Component } from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import Room from "./Room";
import {
  BrowserRouter as Router,  Route, Switch,
  Link,
  Redirect,
} from "react-router-dom";


export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
      <Switch>
          <Route exact path="/">
            <p>Home page</p>
          </Route>
          <Route path='/join'><RoomJoinPage /></Route>
          <Route path='/create'><CreateRoomPage /></Route>
          <Route path='/room/:roomCode' component={Room}></Route>
      </Switch>
      </Router>
    );
  }
}