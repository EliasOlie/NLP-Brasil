import styled from "styled-components";
import { Form as Unform } from '@unform/web';
import COLORS from "./Colors";

const PhraseFormStyle = styled(Unform)`
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;


    input{

        width: 45vw;
        height: 5vh;
        margin-top: 10vh;

        border: none;
        border-radius: 2rem;

        text-align: center;
        background-color: white;
        
    }

    button{
        cursor: pointer;

        margin-top: 1rem;
        width: 15vw;
        height: 5vh;

        border: none;
        border-radius: 1rem;

        font-weight: 600;

        color: #${COLORS.YELLOW};
        background-color: #${COLORS.LIGHTGREEN};
    }

`;

export default PhraseFormStyle