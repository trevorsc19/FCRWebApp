import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import Cookies from 'js-cookie';
import { API_URL } from '../../constants.js'

const Container = styled.div`
    //height: 100vh;
    
    h1 {
        text-align: center;
        color: #4d4d4d;
        font-size: 24px;
        padding: 20px 0 20px 0;
    }
`;

const StyledLoginForm = styled.form`
    width: 300px; 
    margin: 0 auto;
    position: relative;
    top: 50%;
    //border: 2px solid red;
    padding-bottom: 75px;

    input[type="password"],
    input[type="text"] {
        width: 100%;
        padding: 15px;
        border: 1px solid #dddddd;
        margin-bottom: 15px;
        box-sizing: border-box;
    }

    input[type="submit"] {
        width: 100%;
        padding: 15px;
        background-color: #535b63;
        border: 0;
        box-sizing: border-box;
        cursor: pointer;
        font-weight: bold;
        color: #ffffff;
    }
`;

const SubmitButton = styled.div`
    background-color: #4CAF50;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
`;

const LoginForm = (props) => {
    const [userName, setUserName] = useState('lmp004');
    const [password, setPassword] = useState('');

    let handleUserNameInputChange = (e) => {
        setUserName(e.target.value);
    }

    let handlePasswordInputChange = (e) => {
        setPassword(e.target.value);
    }

    function handleLogin(e) {
        console.log("Sending data");
        console.log(JSON.stringify({userName: userName, password: password}));

        fetch(API_URL+"login/", {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({username: userName, password: password})
        })
        .then(response => response.json())
        .then(parsedResponse => {
            console.log('Response', parsedResponse);
            Cookies.set('token', parsedResponse['access_token']);
        });
    }

    return (
        <Container>

            <StyledLoginForm>
                <h1>Login</h1>

                <input type="text" name="username" placeholder="Username" value={userName} required onChange={handleUserNameInputChange} />
                <input type="password" name="password" placeholder="Password" required onChange={handlePasswordInputChange} />
                <SubmitButton onClick={handleLogin}>Submit</SubmitButton>
            </StyledLoginForm>
        </Container>
    )
}

export default LoginForm;