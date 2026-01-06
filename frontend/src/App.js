import React from 'react';
import { motion } from 'framer-motion';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './components/Home';
import About from './components/About';
import Skills from './components/Skills';
import Projects from './components/Projects';
import Certificates from './components/Certificates';
import Contact from './components/Contact';
import ScrollNavigation from './components/ScrollNavigation';
import { ThemeProvider } from './contexts/ThemeContext';

function App() {
  return (
    <ThemeProvider>
      <div className="min-h-screen bg-gray-50 dark:bg-dark-900 transition-colors duration-300">
        <Navbar />
        
        {/* Smooth scrolling sections */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
        >
          <section id="home">
            <Home />
          </section>
          
          <section id="about">
            <About />
          </section>
          
          <section id="skills">
            <Skills />
          </section>
          
          <section id="projects">
            <Projects />
          </section>

          <section id="certificates">
            <Certificates />
          </section>
          
          <section id="contact">
            <Contact />
          </section>
        </motion.div>
        
        <Footer />
        
        {/* Floating scroll navigation */}
        <ScrollNavigation />
      </div>
    </ThemeProvider>
  );
}

export default App;