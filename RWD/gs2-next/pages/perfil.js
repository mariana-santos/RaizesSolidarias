import { Raleway } from 'next/font/google'
const font = Raleway({ subsets: ['latin'] })
import { Quicksand } from 'next/font/google'
const fontBody = Quicksand({ subsets: ['latin'] })

import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';

import '../app/globals.css'
import '../app/styles/perfil.css'

import Menu from '../app/Components/Menu'
import Footer from '../app/Components/Footer'

import { useState } from 'react';

export default function Perfil() {

    const [value, setValue] = useState("geral");

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    return (
        <div className={fontBody.className}>
            <Menu />
            <main className='wrap-profile'>
                <div className='wrap-tabs'>
                    <TabContext value={value} id="tab-context">
                        <TabList onChange={handleChange} aria-label="Perfil do usuário" 
                                 orientation="vertical" variant="fullWidth" className='tab-list'
                                 TabIndicatorProps={{sx: {background: '#685a51'}}}
                        >
                            <Tab label="Dados gerais" value="geral" className='tab' />
                            <Tab label="Área do voluntário" value="voluntario" className='tab' />
                            <Tab label="Área do transportador" value="transportador" className='tab' />
                            <Tab label="Área do doador" value="doador" className='tab' />
                        </TabList>

                        <TabPanel value="geral">Dados gerais</TabPanel>
                        <TabPanel value="voluntario">Área do voluntário</TabPanel>
                        <TabPanel value="transportador">Área do transportador</TabPanel>
                        <TabPanel value="doador">Área do doador</TabPanel>
                    </TabContext>
                </div>
            </main>
            <Footer />
        </div>
    )
}