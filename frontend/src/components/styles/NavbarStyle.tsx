import styled from "styled-components";
import COLORS from "./Colors";

const NavbarStyle = styled.div`

    height: 8vh;
    width: 100vw;
    background-color: #${COLORS.LIGHTGREEN};
    box-shadow: 3px;

    display: flex;
    
   
    a{
        background-color: inherit;
        text-decoration: none;
        padding: 1rem 0;
        margin-left: 1rem;

        color: #${COLORS.YELLOW};
        font-weight: 600

    }

`;

export default NavbarStyle 