import styled from "styled-components";
import COLORS from "./Colors";

const NavbarStyle = styled.div`

    height: 7vh;
    width: 100vw;
    background-color: #${COLORS.LIGHTGREEN};

    padding: 1rem 1rem 0 1rem;

    display: flex;
    
    .nav-wrapper{
        
        background-color: #${COLORS.LIGHTGREEN};

        display: flex;
        flex-direction: row;
    }
   
    a{
        width: 10rem;
        background-color: inherit;
        text-decoration: none;

        color: #${COLORS.YELLOW};
        font-weight: 600

    }

`;

export default NavbarStyle 