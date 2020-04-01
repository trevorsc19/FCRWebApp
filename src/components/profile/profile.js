import React, {useEffect, useState} from 'react';
import styled from 'styled-components';
import { API_URL } from '../../constants.js';
import Cookies from 'js-cookie';
import Editable from '../shared_components/editable.js';

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

const EmailAddressInput = styled.input`
    width: 500px;
`;

const Profile = (props) => {

    const [profileData, setProfileData] = useState('')
    const [task, setTask] = useState("");

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
            <Editable
                text={task}
                placeholder="Write a task name"
                type="input"
            >
                <EmailAddressInput
                    type="text"
                    name="task"
                    placeholder="Wite a task name"
                    value={task}
                    onChange={e => setTask(e.target.value)}
                />

            </Editable>
        </Container>
    )
}

export default Profile;