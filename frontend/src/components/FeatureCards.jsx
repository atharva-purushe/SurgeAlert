import React from 'react'

const FeatureCards = () => {
    return (
        <div className="grid md:grid-cols-3 gap-8">
            <FeatureCard
                title="🎯 Predict Surges Early"
                desc="Forecast OPD/IPD surges 7–21 days in advance using 35 real-time signals including AQI, mobility, festivals, epidemiology, and hospital ops."
            />
            <FeatureCard
                title="🤖 Autonomous Planning"
                desc="5 AI Agents auto-generate rosters, create purchase orders, send deflection SMS, and route patients to less crowded hospitals."
            />
            <FeatureCard
                title="📈 Surge Explanation"
                desc="Explainability via SHAP + LLM: Understand exactly why a surge is coming — AQI, festival proximity, mobility spikes, or outbreaks."
            />
            <FeatureCard
                title="📦 Supply Shortage Predictor"
                desc="Predicts future shortages of oxygen, PPE, beds, and medicines using surge forecasts and consumption trends."
            />
            <FeatureCard
                title="📱Patient Router"
                desc="Advises patients where to go instantly — nearby hospitals ranked by real-time capacity, wait time, specialization."
            />
            <FeatureCard
                title="⚕️ Reduce Overcrowding by 20–30%"
                desc="Operational automation + surge forecasting drastically reduce wait times and overcrowding during critical periods."
            />
        </div>
    )
}

function FeatureCard({ title, desc }) {
    return (
        <div className="p-6 bg-card rounded-xl shadow-sm border border-border hover:shadow-md transition">
            <h4 className="font-semibold text-lg mb-3 text-primary">{title}</h4>
            <p className="text-sm text-muted-foreground leading-relaxed">{desc}</p>
        </div>
    );
}


export default FeatureCards