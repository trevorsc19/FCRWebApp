import React from 'react';
import styles from 'styled-components';

const LoginContainer = styles.div`
    border: 2px solid red;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;

`;

const LoginForm = styles.form`
    input {
        display: block;
    }
`;
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

        fetch("http://127.0.0.1:8000/login", {
            method: "POST", 
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }, 
            body: JSON.stringify({username: this.state.username, password: this.state.password})
        }).then(res=>res.json())
          .then(res => console.log(res));
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