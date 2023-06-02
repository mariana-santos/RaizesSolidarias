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
import DadosGerais from '../app/Components/DadosGerais';
import AreaVoluntario from '../app/Components/AreaVoluntario';
import AreaDoador from '../app/Components/AreaDoador';

import { useEffect, useState } from 'react';
import AreaTransportador from '../app/Components/AreaTransportador';

export default function Perfil() {

    const [value, setValue] = useState("geral");

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    const [orientation, setOrientation] = useState('vertical')

    useEffect(() => {
        if(typeof window !== undefined)
            if(window.innerWidth < 768) setOrientation('horizontal')
    }, [])

    return (
        <div className={fontBody.className}>
            <Menu />
            <main className='wrap-profile'>
                <div className='wrap-tabs'>
                    <TabContext value={value} id="tab-context">
                        <TabList onChange={handleChange} aria-label="Perfil do usuário" 
                                 orientation={orientation} className='tab-list' scrollButtons={false}
                                 TabIndicatorProps={{sx: {background: '#685a51'}}}
                        >
                            <Tab label="Dados gerais" value="geral" className='tab' />
                            <Tab label="Área do voluntário" value="voluntario" className='tab' />
                            <Tab label="Área do transportador" value="transportador" className='tab' />
                            <Tab label="Área do doador" value="doador" className='tab' />
                        </TabList>

                        <TabPanel value="geral" className='tab-content'>
                            <DadosGerais />
                        </TabPanel>
                        <TabPanel value="voluntario" className='tab-content'>
                            <AreaVoluntario />
                        </TabPanel>
                        <TabPanel value="transportador" className='tab-content'>
                            <AreaTransportador />
                        </TabPanel>
                        <TabPanel value="doador" className='tab-content'>
                            <AreaDoador />
                        </TabPanel>
                    </TabContext>
                </div>
            </main>
            <Footer />
        </div>
    )
}