import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import TextField from '@material-ui/core/TextField';
import { endpoint } from '../../constants.js'


const Container = styled.div`
    h1 {
        text-align: center;
		color: #4d4d4d;
		font-size: 24px;
		padding: 20px 0 20px 0;
	}
	
	p {
		text-align: center;
	}
`;

const StyledSignInForm = styled.form`
    width: 300px;
    margin: 0 auto;
    // border: 2px solid blue;
    border-radius: 5px;

	/*
    input[type="password"],
	input[type="text"] {
		width: 100%;
		padding: 15px;
		border: 1px solid #dddddd;
		margin-bottom: 15px;
		box-sizing:border-box;
	}
	*/
    
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
`

const RegisterForm = (props) => {

	const [userName, setUserName] = useState('');
	const [password, setPassword] = useState('');
	const [email, setEmail] = useState('');


	let handleUserNameInputChange = (e) => {
		setUserName(e.target.value);
	}

	let handlePasswordInputChange = (e) => {
		setPassword(e.target.value);
	}

	let handleEmailInputChange = function(e) {
		setEmail(e.target.value);
	}

    let handleLogin = (e) => {
		console.log("Sending data");
		console.log(userName);
		console.log(password);
		fetch(endpoint+"register/", {
			method: 'POST',
			headers: {
				'Accept':'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({userName: userName, password: password, email: email})
		})
		.then(response => response.json())
		.then(response => {
			console.log('Response', response);
		});

    }

    return (
        <Container>
            <h1>Register</h1>
			<p>Please create an account</p>

            <StyledSignInForm>
				<TextField id="outlined-basic" label="Username" variant="outlined" required onChange={handleUserNameInputChange} />
				<TextField id="outlined-basic" label="Password" variant="outlined" type="password" required onChange={handlePasswordInputChange} />
				<TextField id="outlined-basic" label="Email" variant="outlined" required onChange={handleEmailInputChange} />
				<SubmitButton onClick={handleLogin}>Submit</SubmitButton>
            </StyledSignInForm>
        </Container>
    );
}

export default RegisterForm;
