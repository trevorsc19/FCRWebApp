import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import ReactStopwatch from 'react-stopwatch';

const Container = styled.div`
    p {
        text-align: center;
        font-size: 150%;
    }
`

const Timer = (props) => {

    return (
        <ReactStopwatch
            seconds={0}
            minutes={0}
            hours={0}
            limit="00:00:10"
            onChange={({ hours, minutes, seconds }) => {
                // do something
            }}
            onCallback={() => console.log('Finish')}
            render={({ formatted, hours, minutes, seconds }) => {
                return (
                    <Container>
                        <p> {formatted} </p>
                    </Container>
                );
            }}
        />
    );


    /*
    return (
        <Container>
            <p>{currentTime}</p>
        </Container>
    );
    */

}

export default Timer;