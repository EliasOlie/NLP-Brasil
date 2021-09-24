import styled from "styled-components";
import { Form as Unform } from '@unform/web';

const PhraseFormStyle = styled(Unform)`
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;

    input{
        background-color: white;
        
    }

    button{
        margin-top: 1rem;
    }

`;

export default PhraseFormStyle