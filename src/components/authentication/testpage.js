// File used to test JWT and Cookie

import React from 'react';
import Cookie from 'js-cookie';
import styled from 'styled-components';
import { API_URL } from '../../constants.js';

const Container = styled.div`
    p {
        word-break: break-all;
    }

    .protected-route-button {
        display: inline-block;
        border: 2px solid red;
        cursor: pointer;
    }
`;

const ButtonsContainer = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
`;

const Button = styled.div`
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-direction: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
`;

const DeleteCookiesButton = styled(Button)`
    background-color: #4CAF50;
`;

const SendTokenButton = styled(Button)`
    background-color: #38ACEC;
`;

class TestPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            "access_token_cookie": Cookie.get("csrftoken") ? Cookie.get("csrftoken") : null,
            "user_info": null
        }
        this.deleteCookies = this.deleteCookies.bind(this);
        this.sendToken = this.sendToken.bind(this);
        this.sendRequestToProtectedRoute = this.sendRequestToProtectedRoute.bind(this);
    }

    deleteCookies() {
        Cookie.remove('token');
        console.log("Token deleted");
    }

    componentDidUpdate() {
        console.log("Updating complete");
        console.log("USER INFO", this.state.user_info);
    }

    sendToken() {
        console.log('Sending token...', this.state.cookie);

        fetch(API_URL+"tokentest/", {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${this.state.cookie}`
            }
        })
        .then(response => response.json())
        .then(response => {
            this.setState({ user_info: response })
        });

    }

    componentDidMount() {
        console.log("MOUNTED");
        console.log(this.state.cookie);
    }

    sendRequestToProtectedRoute() {
        fetch(API_URL + "sessiontest/", {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(response => console.log(response));
    }

    render() {
        return(
            <Container>
                <h1>Test Page</h1>
                <p>access token: {this.state.access_token_cookie}</p>
                <ButtonsContainer>
                    <DeleteCookiesButton onClick={this.deleteCookies}>Delete Cookie</DeleteCookiesButton>
                    <SendTokenButton onClick={this.sendToken}>Send Token</SendTokenButton>
                </ButtonsContainer>
                <div className="protected-route-button" onClick={this.sendRequestToProtectedRoute}>Send request to protected route</div>
            </Container>
        )
    }
}

export default TestPage;