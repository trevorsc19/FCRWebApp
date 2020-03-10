import React from 'react';
import styles from 'styled-components';
import Cookies from 'universal-cookie';
import { API_URL } from '../../constants.js'

const LoginContainer = styles.div`
    border: 2px solid red;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;

`;

const LoginForm = styles.div`
    input {
        display: block;
    }
`;

const cookies = new Cookies();

class LoginBox extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            username: '', 
            password: ''
        }
        this.onSubmit = this.onSubmit.bind(this);
        this.onUsernameInputChange = this.onUsernameInputChange.bind(this);
        this.onPasswordInputChange = this.onPasswordInputChange.bind(this);
    }

    onSubmit = () => {
        // send password to backend in a fetch() request
        console.log("Submitting");

        //get initial token
        // fetch('http://127.0.0.1:800/login', {
        //     method: "POST", 
        //     credentials: 'same-origin'

        // }).then(() => {
        //     let cookie = cookies.get('csrftoken');
        //     console.log("COOKIE", cookie);
        // }).catch(error=>console.log("darn an error"));

        var bearer_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzMwMzcsImVtYWlsIjoidGVzdGVAZ21haWwuY29tIiwiZXhwIjoxNTc1MjQwNjYyLjY1Mjk0MzF9.10gHpF6gQ3K-XIijFxDwPu5N5gTrg4C-N2wFBt5L_zc';
        var bearer = 'Bearer ' + bearer_token;
        fetch(API_URL+"login/", {
            method: "POST", 
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                //'Authorization': bearer
            }, 
            body: JSON.stringify({username: this.state.username, password: this.state.password})
        }).then(function(response) {
            console.log(response.status)
            console.log(response);
            return response;
        })
          .then(res=>res.json())
          .then(parsed => console.log(parsed))
          .catch(error => alert(error))
          //.catch(error => console.log("request failed with error", error))
    }

    onUsernameInputChange(e) {
        this.setState({ username: e.target.value }, function() {
            console.log("Username change", this.state.username);
        });
    }

    onPasswordInputChange(e) {
        this.setState({ password: e.target.value }, function() {
            console.log("Password change", this.state.password);
        });
    }

    render() {
        return (
            <LoginContainer>
                <LoginForm>
                    <label>Username</label>
                    <input onChange={this.onUsernameInputChange} type="text" name="username" />
                    <label>Password</label>
                    <input onChange={this.onPasswordInputChange} type="password" name="password" />
                    <button onClick={this.onSubmit}>Submit</button>
                </LoginForm>
            </LoginContainer>


        );
    }
}

export default LoginBox;