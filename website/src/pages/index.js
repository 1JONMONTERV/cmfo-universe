import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import styles from './index.module.css';

export default function Home() {
  return (
    <Layout
      title="CMFO–UNIVERSE v∞"
      description="Computación, Física y Lenguaje Unificados en un Autómata Fractal 7D"
    >
      <header className={styles.heroBanner}>
        <div className="container">
          <h1 className={styles.title}>CMFO–UNIVERSE v∞</h1>
          <p className={styles.subtitle}>
            Computación, Física y Lenguaje Unificados en un Autómata Fractal 7D
          </p>

          <div className={styles.buttons}>
            <Link
              className="button button--primary button--lg"
              to="/docs/intro"
            >
              Entrar al Documento Maestro CMFO
            </Link>

            <Link
              className="button button--secondary button--lg"
              to="https://github.com/1jonmonterv/cmfo-universe"
            >
              Repositorio en GitHub
            </Link>
          </div>
        </div>
      </header>

      <main className={styles.mainSection}>
        <section className={styles.section}>
          <h2>¿Qué es el CMFO?</h2>
          <p>
            El Modelo Fractal CMFO es un sistema unificado que integra física fundamental,
            computación fractal, teoría de números, dinámica toroidal y arquitectura algorítmica 7D.
            Todo el conocimiento se deriva desde una estructura geométrica exacta basada en la proporción áurea φ.
          </p>
        </section>

        <section className={styles.sectionAlt}>
          <h2>Arquitectura Fractal 7D</h2>
          <p>
            El CMFO se ejecuta sobre un toro fractal T⁷<sub>φ</sub>, donde cada operación se representa
            como un flujo geométrico autosimilar. Desde SHA-256 hasta QFT fractal, toda computación se
            expresa como trayectorias internas del autómata φ.
          </p>
        </section>

        <section className={styles.section}>
          <h2>GPU, CUDA y Computación Exacta</h2>
          <p>
            El proyecto incluye kernels CUDA, pipelines científicos, álgebra lineal 7D optimizada,
            tokenización fractal, minería determinista y una biblioteca científica unificada para ejecutar
            el universo fractal en hardware real.
          </p>
        </section>

        <section className={styles.sectionAlt}>
          <h2>Documentación Científica</h2>
          <p>
            Este sitio contiene el documento maestro del CMFO, las demostraciones matemáticas,
            pruebas empíricas, derivaciones exactas de constantes físicas y el manifiesto completo.
          </p>

          <Link
            className="button button--primary button--lg"
            to="/docs/intro"
          >
            Abrir Documentación
          </Link>
        </section>
      </main>
    </Layout>
  );
}
