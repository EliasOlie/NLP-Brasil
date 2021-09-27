import NavbarStyle from './styles/NavbarStyle';
import NlStyle from './styles/NavLinkStyle';

export default function Navbar() {
    return (
        <NavbarStyle>
                <a href="/">{"<NLP/> Brasil"}</a>
                <NlStyle>
                    <ul>
                        <li>
                            <a href="/contato">Contato</a>
                        </li>
                    </ul>
                    <ul>
                        <li>
                            <a href="/sobre">Sobre</a>
                        </li>
                    </ul>
                </NlStyle>
        </NavbarStyle>
        


    );
}