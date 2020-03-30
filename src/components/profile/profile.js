import React, {useEffect, useState} from 'react';
import styled from 'styled-components';
import { API_URL } from '../../constants.js';
import Cookies from 'js-cookie';

const Container = styled.div`
    h1 {
        text-align: center;
    }
`;

const LogOutButton = styled.div`
    cursor: pointer;
    position: absolute;
    right: 0;
`;

const Profile = (props) => {

    const [profileData, setProfileData] = useState('')

    useEffect(() => {
        fetch(API_URL+"sessions/profile", {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            credentials: 'include'
        })
        .then(response => response.json())
        .then(parsedResponse => {
            console.log('Response', parsedResponse);
            setProfileData(parsedResponse)
        });
    }, []); 

    function handleLogout(e) {
        console.log("Logging out...");
        fetch(API_URL+"logout/", {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': Cookies.get('csrftoken')
            },
            credentials: 'include'
        })
        //.then(response => response.json())
        .then(response => response.text())
        .then(parsedResponse => {
            console.log('Response', parsedResponse);
        });
    }

    return (
        <Container>
            <LogOutButton onClick={handleLogout}>Logout</LogOutButton>
            <h1>User Profile</h1>
            <h2>Welcome, {profileData.first_name}</h2>
        </Container>
    )
}

export default Profile;