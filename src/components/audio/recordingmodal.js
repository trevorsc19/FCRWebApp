import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { ReactMic } from 'react-mic';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlayCircle, faMicrophone } from '@fortawesome/free-solid-svg-icons';

const StyledRecordingModal = styled.div`
    display: ${props => {
        if (props.showModal === true)
            return 'block';
        else 
            return 'none';
    }}
    width: 500px;
    border: 2px solid red;
`;


const PlayCircle = styled(FontAwesomeIcon)`
`;

const AudioRecordingModal = (props) => {
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
        <StyledRecordingModal showModal = {props.showModal}>
            
            <h1>Record new pitch</h1>

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
            <button onClick={stopRecording} type="button">Stop</button>
            {audioPlayer}
            <PlayCircle icon={faPlayCircle} size="5x" />

        </StyledRecordingModal>
    )
}

export default AudioRecordingModal;