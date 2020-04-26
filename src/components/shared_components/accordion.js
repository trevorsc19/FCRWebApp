import React, { useState } from 'react';
import styled from 'styled-components';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSortUp } from '@fortawesome/free-solid-svg-icons';

const StyledAccordion = styled.div`
    color: #444;
    cursor: pointer;
    border: none;
    outline: none;
    border: 1px solid rgba(0, 0, 0, .125);
    border-radius: 5px;
`;

const Content = styled.div`
    //display: ${props => props.show ? 'block' : 'none'};
    height: ${props => props.show ? '100px' : '0px'};
    background-color: #fff;
    transition: height 0.6s ease;
    overflow: hidden;
`;

const Title = styled.div`
    padding: 18px;
    background-color: ${props => props.show ? '#ccc' : '#eee'};
    &:hover {
        background-color: #ccc;
    }
`;

const stylesForIcons = {
    position: 'absolute', 
    right: '0', 
    top: 0,
    border: '2px solid red'
};

const Accordion = (props) => {
    //array destructuring 
    const [showCollapsible, setShowCollapsible] = useState(false);

    let handleClick = () => {
        setShowCollapsible(!showCollapsible);
    }

    let showPreview = () => {
        console.log('showing preview')
    }

    return (
        <StyledAccordion onClick={handleClick}>
            <Title show={showCollapsible} onMouseEnter={showPreview}>
            <FontAwesomeIcon icon={faSortUp} />
            {props.title}
            </Title>
    
            <Content show={showCollapsible}>
                {props.content} // use props.children instead
            </Content>
        </StyledAccordion>
    )
}

export default Accordion;