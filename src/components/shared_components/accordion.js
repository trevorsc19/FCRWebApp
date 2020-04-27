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
            </Title>
    
            <Content show={showCollapsible}>
                {props.children}
            </Content>
        </StyledAccordion>
    )
}

export default Accordion;