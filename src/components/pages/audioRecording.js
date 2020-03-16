import React, { useState, useEffect } from "react";
import styled from 'styled-components';
import Preloader from "./../preloader";
import Navbar from "./../navbar";
import { ReactMic } from 'react-mic';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlayCircle, faMicrophone } from '@fortawesome/free-solid-svg-icons';
import AudioRecordingModal from '../audio/recordingmodal.js';

const Container = styled.div`

`;

const RecordIcon = styled(FontAwesomeIcon)`
    color: #F50057;
    cursor: pointer;
    
    &:hover {
        color: #8B0000;
    }
`;

const AudioRecording = (props) => {

    const [showRecordingModal, setShowRecordingModal] = useState(false);

    let startRecording = () => setShowRecordingModal(true);

    return (
        <Container>
            <RecordIcon onClick={startRecording} icon={faMicrophone} size="5x" />
            <AudioRecording showModal={showRecordingModal} />
        </Container>
    )
}

export default AudioRecording;