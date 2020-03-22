import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { ReactMic } from 'react-mic';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlayCircle, faMicrophone, faTrash, faSave } from '@fortawesome/free-solid-svg-icons';
import Timer from '../audio/timer.js';
import { UPLOAD_AUDIO_URL } from '../../constants.js';

const StyledRecordingModal = styled.div`
    background-color: #212121;
    display: ${props => {
        if (props.showModal === true) {
            console.log('Showing modal...');
            return 'block';
        }
        else {
            return 'none';
        }
    }}
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

    h1 {
        color: #FFFFFF;
    }

    #date {
        display: inline-block;
        width: 100%;
        text-align: center;
    }
`;


const PlayCircle = styled(FontAwesomeIcon)`
`;

// so we can center the Record Icon 
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

/* BUTTONS ROW*/

const ButtonsRow = styled.div`
    display: ${props => props.showButtonsRow ? 'flex' : 'none'};
    justify-content: center;
    margin: 0 -5px;
    margin-top: 25px;
    margin-bottom: 25px;
`;

const TrashIcon = styled(FontAwesomeIcon)`
`;

const SaveIcon = styled(FontAwesomeIcon)`

`;

const Button = styled.div`
    color: #FFFFFF
    border: 2px solid black;
    margin: 0 5px;
    border-radius: 5px;
    padding: 7px;
    transition: 0.3s;
`

const DeleteButton = styled(Button)`
    cursor: pointer;
    background-color: #DC3545;

    &:hover {
        background-color: #B72C3A
    }
`;

const StopButton = styled(Button)`
    cursor: pointer;
`;

const SaveButton = styled(Button)`
    background-color: #007BFF;
    cursor: pointer; 

    &:hover {
        background-color: #005EC4;
    }
`;

const AudioPlayer = styled.audio`

`;

const AudioRecordingModal = (props) => {
    const [record, setRecord] = useState(false); // start recording
    const [blob, setBlob] = useState(''); // save the blob URL
    const [showAudioPlayer, setShowAudioPlayer] = useState(false); // show the media player to listen to recorded audio 
    const [showButtonsRow, setShowButtonsRow] = useState(false); // show delete, stop and save buttons
    const [showTimer, setShowTimer] = useState(false);

    let startRecording = () => {
        console.log('recording...');
        setRecord(true);
        setShowTimer(true);
        setShowButtonsRow(true);
    }

    // When the 'stop' button is clicked
    function stopRecording() {
        setRecord(false)
    }

    function onData(recordedBlob) {
        console.log('Chunk of real-time data is: ', recordedBlob);
    }

    // When react-mic stops recording
    function onStop(recordedBlob) {
        console.log('recordedBlob is: ', recordedBlob);
        console.log('URL', recordedBlob.blobURL);
        setBlob(recordedBlob.blobURL);
        setShowAudioPlayer(true);
    }

    function onSave() {
        //console.log("Sending the following data", JSON.stringify({audio: blob}));
        console.log("Sending the following data", JSON.stringify({"hi":"hi2"}));
        fetch(UPLOAD_AUDIO_URL, {
            method: 'POST',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
              //'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({"hi":"hi2"})
            // body: JSON.stringify({audio: blob})
          })
            .then(response => {
                console.log("STATUS CODE", response.status);
                console.log(response);
                return response.json();
            })
            .then(parsedResponse => {
              console.log(parsedResponse); 
            }).catch(error => console.log("ERROR", error));
    }

    let audioPlayer;

    if (showAudioPlayer === true) {
        audioPlayer = <AudioPlayer controls="controls" src={blob} type="audio/wav" />
    } else {
        audioPlayer = null;
    }

    let timer;
    let date;

    if (showTimer === true) {
        timer = <Timer />;
        date = <span id="date">{ new Date().toDateString() }</span>
    } else {
        timer = null;
        date = null;
    }

    return (
        <StyledRecordingModal showModal={props.showModal}>
            
            <h1>Record new pitch</h1>

            <ReactMic
                record={record}
                pause={false}
                onStop={onStop}
                onData={onData}
                strokeColor={'#009DFF'}
                backgroundColor={'#212121'}
                visualSetting="sinewave"
                mimeType={'audio/wav'}
                bufferSize={'2048'}
                sampleRate={'44100'}
                audioBitsPerSecond
            />

            { audioPlayer }
            {/* <PlayCircle icon={faPlayCircle} size="5x" /> */}
            { timer }
            { date }
            <RecordIconContainer>
                <RecordIcon onClick={startRecording} icon={faMicrophone} size="5x" />
            </RecordIconContainer>
            <ButtonsRow showButtonsRow={showButtonsRow}>
                <DeleteButton>
                    <TrashIcon icon={faTrash} size="1x" />
                    Delete
                </DeleteButton>
                <StopButton onClick={stopRecording}>Stop</StopButton>
                <SaveButton onClick={onSave}>
                    <SaveIcon icon={faSave} size="1x" />
                    Save
                </SaveButton>
            </ButtonsRow>


        </StyledRecordingModal>
    )
}

export default AudioRecordingModal;

// prop types