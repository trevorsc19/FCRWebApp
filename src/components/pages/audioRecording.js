import React, { useState, useEffect } from "react";
import styled from 'styled-components';
import Preloader from "./../preloader";
import Navbar from "./../navbar";
import { ReactMic } from 'react-mic';

const Container = styled.div`

`;

const AudioRecording = (props) => {
    const [record, setRecord] = useState(false);
    const [blob, setBlob] = useState('');
    const [showAudioPlayer, setShowAudioPlayer] = useState(false);

    let startRecording = () => {
        console.log('recording...');
        setRecord(true);
    }

    function stopRecording() {
        setRecord(false)
    }

    function onData(recordedBlob) {
        console.log('Chunk of real-time data is: ', recordedBlob);
    }

    function onStop(recordedBlob) {
        console.log('recordedBlob is: ', recordedBlob);
        console.log('URL', recordedBlob.blobURL);
        setBlob(recordedBlob.blobURL);
        setShowAudioPlayer(true);
    }

    let audioPlayer;

    if (showAudioPlayer === true) {
        audioPlayer = <audio controls="controls" src={blob} type="audio/wav" />
    } else {
        audioPlayer = null;
    }


    return (
        <Container>
            <ReactMic
                record={record}
                pause={false}
                onStop={onStop}
                onData={onData}
                strokeColor={'#000000'}
                backgroundColor={'#FF4081'}
                mimeType={'audio/wav'}
                bufferSize={'2048'}
                sampleRate={'44100'}
            />
            <button onClick={startRecording} type="button">Start</button>
            <button onClick={stopRecording} type="button">Stop</button>
            {audioPlayer}
        </Container>
    )
}

export default AudioRecording;