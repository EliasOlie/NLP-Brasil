import image from './media/logo.svg'
import NavbarStyle from './styles/NavbarStyle';

export default function Navbar() {
    return (
        <NavbarStyle>
            <div className="nav-wrapper">
                <a href="/"><img src={image} alt="<NLP/> Brasil"/></a>
                <div className="navb">
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
                </div>
            </div>
        </NavbarStyle>
        


    );
}