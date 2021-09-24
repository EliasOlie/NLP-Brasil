import { useState } from "react";

//Midia
import ArrowDown from "./media/arrow-down.svg"

function DropdownItem(props:any){
    return(
        <NavBar>
            <NavItem icon={ArrowDown}>
                <DropDownMenu 
                Polaridade={props.Polaridade}
                Confianca ={props.Confianca}
                NumeroPalavras ={props.NumeroPalavras}
                PalavrasCon = {props.PalavrasCon}
                PalavrasDesc ={props.PalavrasDesc}
                Mensagem={props.Mensagem}
                                
                />
            </NavItem>
        </NavBar>
    );
};

function NavBar(props:any){
    return(
        <nav className='navbar'>
            <div className='navbar-nav'>{ props.children }</div>
        </nav>
    );
};

function NavItem(props:any){

    const [open, setOpen] = useState(false);

    return(
        <div className='nav-item'>
            <div className='Detalhes'>Estatiscas para nerds</div>
            <a href="/#" className='icon-button' onClick={() => setOpen(!open)}><img src={props.icon} alt='Down Arrow'/></a>
            {open && props.children}
        </div>
    );
};

function DropDownMenu(props:any){
    
    function DropDownItem(props:any){
        return(
            <p className='menu-item'>
                {props.children}
            </p>
        );
    };
    
    return(
        <div className="dropdown">
            <DropDownItem>Polaridade: {props.Polaridade}</DropDownItem>
            <DropDownItem>Confiança: {props.Confianca}</DropDownItem>
            <DropDownItem>Numero de palavras: {props.NumeroPalavras}</DropDownItem>
            <DropDownItem>Palavras conhecidas: {props.PalavrasCon}</DropDownItem>
            <DropDownItem>Palavras desconhecidas: {props.PalavrasDesc}</DropDownItem>
            <DropDownItem>Mensagem: {props.Mensagem}</DropDownItem>
        </div>
    );
};

export default DropdownItem