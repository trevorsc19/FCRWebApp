import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import Home from "./components/pages/home";
import Contact from "./components/pages/contact";
import LoginRegister from "./components/pages/loginregister";
import { API_URL } from './constants.js';
import styled from 'styled-components';
import Cookies from 'js-cookie';
import TestPage from './components/authentication/testpage.js'
import AudioRecording from './components/pages/audioRecording.js'
import Profile from './components/profile/profile.js';

import {
    BrowserRouter as Router,
    Route,
    Link,
    Redirect,
    Switch
} from 'react-router-dom';

// here we would get the cookie and check to see if they are authenticated
// https://stackoverflow.com/questions/58109007/react-router-jwt-protect-routes
const PrivateRoute = ({ component: Component, ...rest }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(null);
    const [userid, setUserId] = useState();
  
    // in actaulity, this would only be set after a successful login
    //Cookies.set('token', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOjU1NSwidXNlcm5hbWUiOiJhYjUwNSIsImFkbWluIjp0cnVlLCJpYXQiOjE1Nzk4ODE5NDYsImV4cCI6MTU3OTkxMTk0Nn0.CNtEVna-pZlslDEM94W1whJRIZFnJrNVla3svgu9jfs');
    //Cookies.set('token', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOjU1NSwiYWRtaW4iOnRydWUsImlhdCI6MTU3OTcxOTY0NSwiZXhwIjoxNTc5NzQ5NjQ1fQ.Dj6SncqRbPe-KG0rcoxDpnXmw0c4n53zAYrIGVU87M');
  
    useEffect(() => {
  
      // token is only ever set when user successfully logins in 
      let token = Cookies.get('token');
      console.log("PRIVATE ROUTE COOKIE:", token);
  
      if (token) {
        //setIsAuthenticated(true);
        //send to server to verify it 
  
        fetch(API_URL+'/verifytoken', {
          method: 'GET',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          }
        })
          .then(response => {
              console.log(response.status);
            if (response.status === 401) {
              console.log('Token expired');
              setIsAuthenticated(false);
            } else if (response.status === 200) {
              console.log("SETTING USER IS AUTHENTICATED");
              setIsAuthenticated(true)
            } else {
              console.log("NOT AUTHENITCTED");
              setIsAuthenticated(false);
            }
            return response.json();
          })
          .then(response => {
            //console.log(response); 
            setUserId(response);
          }).catch(error => console.log("ERROR", error));
  
      } else {
        console.log("Token not found");
        setIsAuthenticated(false);
      }
  
    }, [isAuthenticated])
  
    console.log("ABOUT TO RETURN");
    console.log("IS AUTHENTICATED?", isAuthenticated);
  
    if (isAuthenticated === null) {
      return <></>
    }
  
    return (
      <Route {...rest} render={(props) => (
        isAuthenticated === true ? <Component {...props} /> : <Redirect to="/login" />
      )} />
    )
  
  }

const NotFound = () => {
    return <h1>404 NOT FOUND</h1>;
}

const Container = styled.div`
`;

// everything to the right of the side bar 
const Main = styled.main`
  margin-left: 200px;
`;

const Hello = () => {
    return (
        <Container>
            <Main>
                <h1>Hello</h1>
            </Main>
        </Container>
    )
}

const HelloThere = () => {
    return (
        <Container>
            <Main>
                <h1>Hello There</h1>
            </Main>
        </Container>
    )
}

const Protected = () => {
    //console.log("REDUX", this.props);

    return (
        <Container>
            <Main>
                <h1>You are signed in, </h1>
            </Main>
        </Container>
    )

}

function App() {

    return (
        // https://stackoverflow.com/questions/50584641/invariant-violation-you-should-not-use-switch-outside-a-router
        <Router>
            <Switch>
                <Route exact path="/" component={Home} />
                <Route path="/login" component={LoginRegister} />
                <Route path="/contact" component={Contact} />
                <Route path="/test" component={TestPage} />
                <Route path="/hellothere" component={HelloThere} />
                <Route path="/hi" component={() => <h1>hi</h1>} />
                <Route path="/audio" component={AudioRecording} />
                <Route path="/profile" component={Profile} />
                <PrivateRoute path="/hello" component={Hello} />
                <PrivateRoute path='/protected' component={Protected} />
                <Route path="/404" component={NotFound} />
                <Redirect to="/404" />
            </Switch>
        </Router>

    );
}

ReactDOM.render(<App />, document.getElementById('root'));

