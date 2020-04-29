import React, { useState } from 'react';
import styled from 'styled-components';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSortUp } from '@fortawesome/free-solid-svg-icons';

const StyledAccordion = styled.div`
    // so 'AccordionArrow' can abe positioned absolutely
    position: relative;
    color: #444;
    cursor: pointer;
    border: none;
    outline: none;
    border: 1px solid rgba(0, 0, 0, .125);
    border-radius: 5px;
`;

const Content = styled.div`
    //display: ${props => props.show ? 'block' : 'none'};
    // https://stackoverflow.com/a/8331169
    max-height: ${props => props.show ? '150px' : '0px'};
    transition: max-height 0.6s ease;
    overflow: hidden;
    background-color: #fff;
`;

const Title = styled.div`
    // so Date could be positioned absolutely
    position: relative;
    padding: 18px;
    background-color: ${props => props.show ? '#ccc' : '#eee'};
    &:hover {
        background-color: #ccc;
    }

    .date {
        position: absolute;
        left: 0;
        bottom: 0;
        display: inline-block;
        //border: 2px solid red;
        font-size: 50%;
    }
`;

const AccordionArrow = styled(FontAwesomeIcon)`
    position: absolute;
    right: 15px;
    top: 0;
    transform: ${props => props.rotateArrow ? 'rotate(180deg)' : 'rotate(90deg)'};
    transition: transform 0.5s;
    font-size: 50px;
`;



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
            <AccordionArrow rotateArrow={showCollapsible} icon={faSortUp} />
            {props.title}
            <span class="date">{new Date().toISOString().slice(0,10)}</span>
            </Title>
    
            <Content show={showCollapsible}>
                {props.children}
            </Content>
        </StyledAccordion>
    )
}

export default Accordion;