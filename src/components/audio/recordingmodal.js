import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { ReactMic } from 'react-mic';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlayCircle, faMicrophone } from '@fortawesome/free-solid-svg-icons';

const StyledRecordingModal = styled.div`
    display: ${props => {
        if (props.showModal === true) {
            console.log('Showing modal...');
            return 'block';
        }
        else {
            return 'none';
        }
    }}
    border: 2px solid red;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
`;


const PlayCircle = styled(FontAwesomeIcon)`
`;

const RecordIconContainer = styled.div`
    display: flex;
    justify-content: center;
`;

const RecordIcon = styled(FontAwesomeIcon)`

    color: #F50057;
    cursor: pointer;
    
    &:hover {
        color: #8B0000;
    }
`;

const ButtonsRow = styled.div`
    display: ${props => props.showButtonsRow ? 'flex' : 'none'};
    border: 2px solid blue;
    justify-content: center;
`;


const DeleteButton = styled.div`
    cursor: pointer;
`;

const StopButton = styled.div`
    cursor: pointer;
`;

const SaveButton = styled.div`
    cursor: pointer;
`;

const AudioRecordingModal = (props) => {
    const [record, setRecord] = useState(false);
    const [blob, setBlob] = useState('');
    const [showAudioPlayer, setShowAudioPlayer] = useState(false);
    const [showButtonsRow, setShowButtonsRow] = useState(false);

    let startRecording = () => {
        console.log('recording...');
        setRecord(true);
        setShowButtonsRow(true);
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
        <StyledRecordingModal showModal={props.showModal}>
            
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

            {audioPlayer}
            {/* <PlayCircle icon={faPlayCircle} size="5x" /> */}
            <RecordIconContainer>
                <RecordIcon onClick={startRecording} icon={faMicrophone} size="5x" />
            </RecordIconContainer>
            <ButtonsRow showButtonsRow={showButtonsRow}>
                <DeleteButton>Delete</DeleteButton>
                <StopButton onClick={stopRecording}>Stop</StopButton>
                <SaveButton>Save</SaveButton>
            </ButtonsRow>


        </StyledRecordingModal>
    )
}

export default AudioRecordingModal;

// prop types