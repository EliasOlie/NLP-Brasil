import { createGlobalStyle } from "styled-components";
import COLORS from "./Colors";

const GlobalStyle = createGlobalStyle`
    *{
        margin: 0;
        padding: 0;
        box-sizing: border-box;

        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        background-color: #${COLORS.DARKGREEN};
        color: black;
    }

`

export default GlobalStyle