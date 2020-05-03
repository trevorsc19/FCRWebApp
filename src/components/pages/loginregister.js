import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import LoginForm from '../authentication/login.js';
import RegisterForm from '../authentication/register.js';
import { API_URL } from '../../constants.js'

const Container = styled.div`
    border: 2px solid red;
    h1 {
        text-align: center;
		color: #4d4d4d;
		font-size: 24px;
		padding: 20px 0 20px 0;
    }
`;

const Tabs = styled.div`
    display: flex;
    justify-content: space-between;
    width: 30%;
    position: relative;
    left: 50%;
    transform: translateX(-50%);
    cursor: pointer;
    //border: 2px solid blue;
    max-width: 600px;
`;

const TabUnderLine = styled.div`
    position: absolute;
    bottom: 0;
    left: ${props => {
        console.log('Props is', props);
        if(props.current_type === 'LogIn') {
            return 0;
        } else if (props.current_type === 'register') {
            return '50%';
        }
    }};
    width: 50%;
    height: 2px;
    background-color: #4A66F4;
    -webkit-transition: left .25s;
    transition: left .25s;
`;

const LoginTab = styled.div`
    //border-bottom: ${props => props.current_type === 'LogIn' ? '5px solid red' : 'none' };
    //transition: color 0.3s;
    flex-basis: 50%;
    text-align: center;
`;

const RegisterTab = styled.div`
    //border-bottom: ${props => props.current_type === 'register' ? '5px solid red' : 'none' };
    //transition: color 2s;
    flex-basis: 50%;
    text-align: center;
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
            <Tabs>
                <LoginTab current_type={form} onClick={showLogInForm}>Log in</LoginTab>
                <RegisterTab current_type={form} onClick={showRegisterForm}>Register</RegisterTab>
                <TabUnderLine current_type={form} />
            </Tabs>
           
            {formToShow}

        </Container>
    );
}

export default LoginRegister;