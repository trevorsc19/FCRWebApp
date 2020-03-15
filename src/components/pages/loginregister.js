import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import LoginForm from '../authentication/login.js';
import RegisterForm from '../authentication/register.js';
import { API_URL } from '../../constants.js'

const Container = styled.div`
    h1 {
        text-align: center;
		color: #4d4d4d;
		font-size: 24px;
		padding: 20px 0 20px 0;
    }
    // https://stackoverflow.com/questions/20626685/better-way-to-set-distance-between-flexbox-items
    .tabs {
        display: flex;
        justify-content: center;
        margin: 0 -5px;

        div {
            margin: 0 5px; 
            cursor: pointer;
        }
    }
`;

const RegisterTab = styled.div`
    border-bottom: ${props => props.current_type === 'register' ? '5px solid red' : 'none' };
`;

const LoginTab = styled.div`
    border-bottom: ${props => props.current_type === 'LogIn' ? '5px solid red' : 'none' };
`;

const LoginRegister = (props) => {

    const [form, setForm] = useState("LogIn");

    useEffect(() => {
        console.log("USE EFFECT");
    });

    function showRegisterForm(e) {
        setForm("register");
    }

    function showLogInForm(e) {
        setForm("LogIn");
    }

    let formToShow;
    if (form === 'register') {
        formToShow = <RegisterForm />
    } else if(form === 'LogIn') {
        formToShow = <LoginForm />
    }


    return (
        <Container>
            <div class="tabs">
                <LoginTab current_type={form} onClick={showLogInForm}>Log in</LoginTab>
                <RegisterTab current_type={form} onClick={showRegisterForm}>Register</RegisterTab>
            </div>
           
            {formToShow}

        </Container>
    );
}

export default LoginRegister;