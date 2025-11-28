import React from "react";
import { useNavigate } from "react-router-dom";
import { SignedIn, SignedOut, UserButton } from "@clerk/clerk-react";
import Navbar from "../components/Navbar";
import FeatureCards from "../components/FeatureCards";
import Footer from "../components/Footer";
export default function LandingPage() {
    const navigate=useNavigate();
  return (
    <div className="min-h-screen bg-background text-foreground font-sans">
      {/* NAVBAR */}
      <Navbar/>

      {/* HERO SECTION */}
      <section className="max-w-7xl mx-auto px-6 py-20">
        <div className="grid lg:grid-cols-2 gap-10 items-center">
          <div>
            <h2 className="text-4xl lg:text-5xl font-extrabold leading-tight mb-6">
              Predictive Hospital Management for India's  
              <span className="text-primary"> Festivals</span>,  
              <span className="text-secondary"> Pollution Spikes</span>, and  
              <span className="text-destructive"> Epidemics</span>.
            </h2>

            <p className="text-muted-foreground text-lg leading-relaxed mb-8">
              Hospitals across India face unpredictable surges during Diwali, Holi,
              winter smog, crop-burning pollution, viral outbreaks, and large
              public gatherings. SurgeShield AI uses multi-signal intelligence and
              autonomous agents to help hospitals prepare, optimize resources, and
              prevent overcrowding before it happens.
            </p>

            <div className="flex gap-4">
              <button className="px-6 py-3 bg-primary text-primary-foreground rounded-lg shadow-md hover:shadow-lg transition">
                View Demo
              </button>
              <button className="px-6 py-3 border border-border rounded-lg hover:bg-muted transition">
                Explore Features
              </button>
            </div>
          </div>

          {/* HERO SIDE VISUAL */}
          <div className="relative">
            <div className="w-full h-80 rounded-xl bg-gradient-to-br from-primary/20 via-secondary/20 to-accent/20 shadow-lg" />
            <div className="absolute inset-0 flex items-center justify-center">
              <p className="text-sm text-muted-foreground">
                (Future: Add a 3D radar animation or Lottie chart here)
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* FEATURES */}
      <section className="max-w-7xl mx-auto px-6 pb-20">
        <h3 className="text-3xl font-bold mb-10 text-center">Why SurgeShield AI?</h3>
        <FeatureCards/>
      </section>

      {/* FOOTER */}
      <Footer/>
    </div>
  );
}
