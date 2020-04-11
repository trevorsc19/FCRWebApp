import React, {useState, useEffect} from 'react';
import styled from 'styled-components';

const Section = styled.section`
    .non-active {
        border-radius: 2px;
        padding-top: 5px;
        padding-bottom: 5px;
        padding-left: 5px;
        padding-right: 5px;
        color: #4A5568;
        line-height: 1.25;

        &:hover {
            border: 4px solid rgba(66, 153, 255, 0.5);
        }
    }
`;

// blog.logrocket.com/the-complete-guide-to-building-inline-editable-ui-in-react/
const Editable = ({text, type, placeholder, children, ...props}) => {
    const [isEditing, setEditing] = useState(false);

    const handleKeyDown = (event, type) => {

    };
    
    return (
        <Section {...props}>
            {isEditing ? (
                <div 
                    onBlur={() => setEditing(false)}
                    onKeyDown={e => handleKeyDown(e, type)}
                >
                    {children}
                </div>
            ) : (
                <div 
                    className='non-active'
                    onClick={() => setEditing(true)}
                >
                    <span>
                        {text || placeholder || "Editable content"}
                    </span>
                
                </div>
            )}
        </Section>
    );

}

export default Editable;