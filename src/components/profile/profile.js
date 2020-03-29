import React, {useEffect, useState} from 'react';
import styled from 'styled-components';

const Container = styled.div`
    h1 {
        text-align: center;
    }
`;

const Profile = (props) => {
    return (
        <Container>
            <h1>User Profile</h1>
        </Container>
    )
}

export default Profile;