import styled from "styled-components";
import COLORS from "./Colors";

const NlStyle = styled.nav`
    display: flex;
    flex-direction: row;
    padding: 0 1rem;
    justify-content: flex-end;
    background-color: inherit;
    
    li{

        list-style: none;

        margin-left: 1rem;

    }
    a{
        text-decoration: none;
        background-color: #${COLORS.LIGHTGREEN};
    }
`;

export default NlStyle