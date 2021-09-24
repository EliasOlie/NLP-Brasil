import styled from "styled-components";
import COLORS from "./Colors";

const NavbarStyle = styled.div`

    height: 7vh;
    width: 100vw;
    background-color: #${COLORS.LIGHTGREEN};

    padding: 1rem 1rem 0 1rem;

    
    .nav-wrapper{
        
        background-color: #${COLORS.LIGHTGREEN};

        display: flex;
        flex-direction: row;
    }

    .navb{
        display: flex;
        justify-content: flex-end
    }

    img{
        width: 8vw;
        background-color: #${COLORS.LIGHTGREEN};

    }

    li{

        list-style: none;
        background-color: #${COLORS.LIGHTGREEN};

    }
    a{
        text-decoration: none;
        background-color: #${COLORS.LIGHTGREEN};


    }
`;

export default NavbarStyle