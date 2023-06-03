import '../app/globals.css'
import Layout from '../app/layout'

import { QueryClientProvider, QueryClient } from 'react-query'

import { ToastContainer } from 'react-toastify'

function MyApp({ Component, pageProps }) {
    const queryClient = new QueryClient()
    
    return (
        // <Layout>
        
        <QueryClientProvider client={queryClient}>
            <Component {...pageProps} >
                <ToastContainer
                    position="bottom-right"
                    autoClose={2000}
                    closeOnClick
                    pauseOnHover
                />
            </Component>
        </QueryClientProvider>
        // </Layout>
    )
}

export default MyApp