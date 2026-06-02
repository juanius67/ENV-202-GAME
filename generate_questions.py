import json

questions = [
    # --- MODULE 1: INTRO & METABOLISM ---
    {
        "q": "Which sequence correctly identifies the four defining characteristics of a microbial metabolism?",
        "c": "Energy source, electron donor, electron acceptor, carbon source",
        "w": [
            "Carbon source, nitrogen source, electron acceptor, energy source",
            "Energy source, proton donor, electron acceptor, nitrogen source",
            "Electron donor, electron acceptor, carbon source, light source"
        ],
        "type": "normal",
        "module": "M01"
    },
    {
        "q": "What is the defining difference between substrate-level phosphorylation (SLP) and oxidative phosphorylation?",
        "c": "SLP makes ATP directly in a pathway without a PMF; oxidative requires an ETC and a PMF.",
        "w": [
            "SLP only occurs in aerobes; oxidative phosphorylation only occurs in anaerobes.",
            "SLP utilizes external electron acceptors like O2; oxidative relies on internal organic acceptors.",
            "SLP generates 30+ ATP per glucose; oxidative phosphorylation yields only ~2 ATP."
        ],
        "type": "normal",
        "module": "M01"
    },
    {
        "q": "Acidithiobacillus ferrooxidans is a chemolithoautotroph. What does this mean?",
        "c": "It uses chemical energy, an inorganic electron donor, and CO2 as its carbon source.",
        "w": [
            "It uses chemical energy, an organic electron donor, and organic carbon.",
            "It uses light energy, an inorganic electron donor, and CO2 as its carbon source.",
            "It uses chemical energy, an inorganic electron donor, and organic carbon."
        ],
        "type": "normal",
        "module": "M01"
    },
    {
        "q": "If a reaction's ONLY electron acceptor is an organic breakdown product of the electron donor, what metabolism is this?",
        "c": "Fermentation",
        "w": [
            "Aerobic Respiration",
            "Anaerobic Respiration",
            "Chemolithotrophy"
        ],
        "type": "normal",
        "module": "M01"
    },
    {
        "q": "For the reaction NO3- + 5e- + 6H+ -> 1/2 N2 + 3 H2O (E0' = +0.74 V) coupled to acetate oxidation (E0' = -0.29 V), what is the formula for calculating ΔE0'?",
        "c": "ΔE0' = E0'(acceptor) - E0'(donor) = +0.74 - (-0.29) = +1.03 V",
        "w": [
            "ΔE0' = E0'(donor) - E0'(acceptor) = -0.29 - (+0.74) = -1.03 V",
            "ΔE0' = E0'(acceptor) + E0'(donor) = +0.74 + (-0.29) = +0.45 V",
            "ΔE0' = E0'(donor) + E0'(acceptor) = -0.29 + (+0.74) = +0.45 V"
        ],
        "type": "normal",
        "module": "M01"
    },
    {
        "q": "In a mixed culture graph, how do you identify the organism driving a transformation?",
        "c": "It is the organism whose substrate is being consumed and product is being produced.",
        "w": [
            "It is the organism that consumes the most oxygen.",
            "It is always the phototroph, if present.",
            "It is the organism that produces the highest amount of CO2."
        ],
        "type": "normal",
        "module": "M01"
    },
    {
        "q": "Look at the reaction: 4 S0 + 4 H2O -> 3 H2S + SO4(2-) + 2 H+. What phenomenon is occurring here?",
        "c": "Disproportionation; the S0 acts as BOTH the electron donor and electron acceptor.",
        "w": [
            "Aerobic respiration; H2O is acting as the terminal electron acceptor.",
            "Oxygenic photosynthesis; water is being split to provide electrons.",
            "Fermentation; S0 is an organic molecule acting as donor and acceptor."
        ],
        "type": "boss",
        "module": "M01"
    },
    {
        "q": "Balance and classify: Lactate + 4 Fe3+ + H2O -> Acetate + CO2 + 4 Fe2+ + 4 H+. What is the net oxidation state change of carbon, and how many electrons are released per lactate?",
        "c": "One C goes from 0 to +4, releasing 4 electrons per lactate. Donor: Lactate, Acceptor: Fe3+.",
        "w": [
            "One C goes from 0 to +4, releasing 8 electrons per lactate. Donor: Acetate, Acceptor: CO2.",
            "Two C go from 0 to +2, releasing 4 electrons per lactate. Donor: Fe3+, Acceptor: Lactate.",
            "One C goes from -2 to +2, releasing 4 electrons per lactate. Donor: Lactate, Acceptor: Fe3+."
        ],
        "type": "boss",
        "module": "M01"
    },

    # --- MODULE 2: ENZYMES ---
    {
        "q": "Which enzyme class catalyzes reactions involving a change in oxidation state, typically involving NAD(P)H or FAD?",
        "c": "Oxidoreductase",
        "w": [
            "Transferase",
            "Hydrolase",
            "Ligase"
        ],
        "type": "normal",
        "module": "M02"
    },
    {
        "q": "How can you distinguish a transferase from a ligase when ATP is involved?",
        "c": "Transferase leaves an ATP fragment (like phosphate) in the product; Ligase uses ATP purely for energy (leaving ADP+Pi or AMP+PPi).",
        "w": [
            "Ligase leaves an ATP fragment in the product; Transferase uses ATP purely for energy.",
            "Transferase always produces AMP; Ligase always produces ADP.",
            "Transferase does not use ATP; Ligase uses ATP to transfer functional groups."
        ],
        "type": "normal",
        "module": "M02"
    },
    {
        "q": "An enzyme catalyzes a reaction with ΔG = +15 kJ/mol. How can the cell make this reaction proceed?",
        "c": "By coupling it to a strongly exergonic reaction, like ATP hydrolysis.",
        "w": [
            "By increasing the enzyme concentration to lower the ΔG.",
            "By waiting longer, as enzymes eventually make endergonic reactions proceed.",
            "By raising the temperature until the ΔG becomes negative."
        ],
        "type": "normal",
        "module": "M02"
    },
    {
        "q": "Bacteria convert AsO4(3-) to AsO3(3-). Determine the As oxidation state in each, and the enzyme class.",
        "c": "As goes from +5 to +3 (reduction). Enzyme class: Oxidoreductase.",
        "w": [
            "As goes from +3 to +5 (oxidation). Enzyme class: Transferase.",
            "As goes from +4 to +2 (reduction). Enzyme class: Lyase.",
            "As goes from +5 to +3 (reduction). Enzyme class: Hydrolase."
        ],
        "type": "boss",
        "module": "M02"
    },

    # --- MODULE 3: ENZYME KINETICS & CHEMOSTAT ---
    {
        "q": "In Michaelis-Menten kinetics, what does a low K_M indicate?",
        "c": "High enzyme affinity for the substrate.",
        "w": [
            "Low enzyme affinity for the substrate.",
            "A high maximum velocity (v_max).",
            "The enzyme is competitively inhibited."
        ],
        "type": "normal",
        "module": "M03"
    },
    {
        "q": "On a Lineweaver-Burk plot, the lines with and without inhibitor cross on the x-axis, but have different y-intercepts. What is the inhibition type?",
        "c": "Non-competitive inhibition (K_M unchanged, v_max decreased)",
        "w": [
            "Competitive inhibition (v_max unchanged, K_M increased)",
            "Uncompetitive inhibition (Both K_M and v_max decreased proportionally)",
            "Mixed inhibition (Both x and y intercepts change)"
        ],
        "type": "normal",
        "module": "M03"
    },
    {
        "q": "In a chemostat at steady state, what does the specific growth rate (μ) equal?",
        "c": "The dilution rate (D = Q/V)",
        "w": [
            "The maximum specific growth rate (μ_max)",
            "The half-saturation constant (K_S)",
            "The specific substrate consumption rate (q_S)"
        ],
        "type": "normal",
        "module": "M03"
    },
    {
        "q": "What happens if you run a chemostat with a dilution rate (D) greater than the organism's μ_max?",
        "c": "Wash-out occurs; cells leave the reactor faster than they can grow.",
        "w": [
            "The biomass concentration reaches a maximum steady state.",
            "The cells adapt and increase their μ_max to match D.",
            "Substrate concentration in the effluent drops to zero."
        ],
        "type": "normal",
        "module": "M03"
    },
    {
        "q": "For a chemostat, the minimum substrate concentration (S_min) to sustain biomass is given by S_min = b·K_S / (μ_max - b). What does 'b' represent?",
        "c": "The maintenance rate (decay coefficient), which must be used directly in the formula.",
        "w": [
            "The yield coefficient (Y), representing biomass per substrate.",
            "The specific substrate consumption rate (q_S).",
            "The dilution rate (D) of the chemostat."
        ],
        "type": "boss",
        "module": "M03"
    },

    # --- MODULE 4: FERMENTATION ---
    {
        "q": "Which of the following is the key diagnostic feature of Homolactic fermentation in a graph?",
        "c": "Only lactate is produced, no gas (CO2) is generated, and pH drops.",
        "w": [
            "Equimolar amounts of ethanol and CO2 are produced.",
            "Hydrogen gas, butyrate, and CO2 are produced.",
            "Lactate, ethanol, and CO2 are produced simultaneously."
        ],
        "type": "normal",
        "module": "M04"
    },
    {
        "q": "Why does the presence of O2 typically halt fermentation?",
        "c": "O2 irreversibly inactivates fermenter enzymes (like pyruvate-formate lyase) and alters redox balance.",
        "w": [
            "O2 acts as a competitive inhibitor at the active site of all kinases.",
            "Fermenting organisms immediately switch to oxidative phosphorylation, which is slower.",
            "O2 consumes all available glucose chemically before the bacteria can."
        ],
        "type": "normal",
        "module": "M04"
    },
    {
        "q": "Secondary fermentation, like that of Propionibacterium (which creates Emmentaler cheese holes), relies on what specific precursor?",
        "c": "Lactate produced by a primary fermenter (like Lactobacillus).",
        "w": [
            "Glucose directly from the environment.",
            "Acetate and formate produced by E. coli.",
            "Ethanol produced by yeast."
        ],
        "type": "normal",
        "module": "M04"
    },
    {
        "q": "In a closed culture of Clostridium, you notice acetone, butanol, and ethanol (ABE) appearing. What physiological shift has occurred?",
        "c": "The culture switched to the solventogenic phase to prevent a lethal pH drop from acid accumulation.",
        "w": [
            "The culture exhausted its carbon source and began consuming its own biomass.",
            "Oxygen leaked into the culture, shifting it to aerobic respiration.",
            "A secondary fermenter took over and began consuming the butyrate."
        ],
        "type": "boss",
        "module": "M04"
    },

    # --- MODULE 5: Fe REDUCTION ---
    {
        "q": "At neutral pH, Fe(III) is highly insoluble. Which is NOT a strategy used by bacteria to deliver electrons to solid Fe(III)?",
        "c": "Phagocytosis of the iron mineral into the cytoplasm.",
        "w": [
            "Direct contact via outer-membrane c-type cytochromes.",
            "Conductive pili (microbial nanowires).",
            "Excretion of diffusible electron shuttles (e.g., flavins)."
        ],
        "type": "normal",
        "module": "M05"
    },
    {
        "q": "When embedded in a gel where direct cell-mineral contact is impossible, Shewanella can reduce Fe(III) using pyruvate but NOT lactate. Why?",
        "c": "Pyruvate fermentation produces H2 (a diffusible shuttle), whereas lactate oxidation requires direct contact.",
        "w": [
            "Lactate is toxic to Shewanella when confined in a gel matrix.",
            "Pyruvate is a stronger electron acceptor than lactate.",
            "The gel matrix binds lactate, preventing it from entering the cell."
        ],
        "type": "normal",
        "module": "M05"
    },
    {
        "q": "Geobacter oxidizes acetate to CO2 using Fe(III). How many electrons are transferred to Fe(III) per molecule of acetate fully mineralized?",
        "c": "8 electrons",
        "w": [
            "4 electrons",
            "2 electrons",
            "12 electrons"
        ],
        "type": "normal",
        "module": "M05"
    },

    # --- MODULE 6: Fe OXIDATION ---
    {
        "q": "Acidithiobacillus ferrooxidans oxidizes Fe2+ at pH 2. Why does it produce massive amounts of Fe(III) while yielding very little biomass?",
        "c": "The ΔE between Fe2+ and O2 is tiny, and it must spend ATP on reverse electron flow to make NADH for CO2 fixation.",
        "w": [
            "It is highly inefficient at capturing light energy for photosynthesis.",
            "Most of the energy is lost as heat to maintain the acidic pH.",
            "It uses fermentation, which has a naturally low ATP yield per Fe2+."
        ],
        "type": "normal",
        "module": "M06"
    },
    {
        "q": "What is the purpose of 'reverse electron flow' in organisms like A. ferrooxidans?",
        "c": "To push electrons uphill against the redox gradient to reduce NAD+ to NADH, powered by PMF.",
        "w": [
            "To generate ATP by pumping protons backward into the cytoplasm.",
            "To safely dispose of excess electrons when O2 is not available.",
            "To reduce Fe3+ back to Fe2+ when iron is limiting."
        ],
        "type": "normal",
        "module": "M06"
    },
    {
        "q": "How does Gallionella avoid entombment in Fe(OH)3 precipitates while oxidizing Fe(II) at neutral pH?",
        "c": "It grows at the tip of an extracellular twisted stalk where the iron oxides deposit.",
        "w": [
            "It excretes strong acids to keep the Fe(III) soluble in its immediate vicinity.",
            "It uses a thick polysaccharide capsule to repel the iron minerals.",
            "It grows inside empty sheaths discarded by other bacteria."
        ],
        "type": "normal",
        "module": "M06"
    },
    {
        "q": "A reactor with 20mM Fe(II) and 10mM NO3- runs until 5mM NO3- and 20mM Fe(II) are consumed. Ratio is 4 Fe(II) : 1 NO3-. What is the N product?",
        "c": "N2O (Nitrous oxide), since NO3- (N at +5) accepts 4 electrons to become N at +1.",
        "w": [
            "N2 (Nitrogen gas), since NO3- accepts 5 electrons.",
            "NH4+ (Ammonium), since NO3- accepts 8 electrons.",
            "NO2- (Nitrite), since NO3- accepts 2 electrons."
        ],
        "type": "boss",
        "module": "M06"
    },

    # --- MODULE 7: PHOTOSYNTHESIS ---
    {
        "q": "In oxygenic photosynthesis, what acts as the electron donor, and what acts as the energy source?",
        "c": "Electron donor: H2O; Energy source: Light",
        "w": [
            "Electron donor: Light; Energy source: CO2",
            "Electron donor: H2S; Energy source: Light",
            "Electron donor: O2; Energy source: Light"
        ],
        "type": "normal",
        "module": "M07"
    },
    {
        "q": "Why do cyanobacteria require a 'Z scheme' (two photosystems in series) for oxygenic photosynthesis?",
        "c": "A single photon excitation cannot span the massive redox gap from H2O (+0.82V) to NADP+ (-0.32V).",
        "w": [
            "One photosystem produces ATP while the other exclusively fixes CO2.",
            "PS II is only active during the day, while PS I is active at night.",
            "PS I oxidizes water, but it needs PS II to pump protons for the PMF."
        ],
        "type": "normal",
        "module": "M07"
    },
    {
        "q": "Which characteristic perfectly distinguishes a Type I Reaction Center (RC I) from a Type II (RC II)?",
        "c": "RC I reduces ferredoxin directly (making NADH), while RC II reduces quinones and requires reverse electron flow.",
        "w": [
            "RC I produces oxygen, while RC II produces sulfur.",
            "RC I is found only in Archaea, while RC II is found in Bacteria.",
            "RC I performs cyclic electron flow, while RC II performs linear electron flow."
        ],
        "type": "normal",
        "module": "M07"
    },
    {
        "q": "What massive light-harvesting structures allow Green Sulfur bacteria (Chlorobium) to grow at depths where almost no light penetrates?",
        "c": "Chlorosomes",
        "w": [
            "Phycobilisomes",
            "Carboxysomes",
            "Anammoxosomes"
        ],
        "type": "normal",
        "module": "M07"
    },

    # --- MODULE 8: CO2 FIXATION ---
    {
        "q": "Which CO2 fixation pathway is the most energetically cheap (~1 ATP per pyruvate) but can only be used by strict anaerobes due to an O2-sensitive CO-dehydrogenase?",
        "c": "Wood-Ljungdahl Pathway",
        "w": [
            "Calvin (CBB) Cycle",
            "rTCA (Arnon-Buchanan) Cycle",
            "3-HP bi-cycle"
        ],
        "type": "normal",
        "module": "M08"
    },
    {
        "q": "What is the primary function of a carboxysome in cyanobacteria?",
        "c": "To concentrate CO2 around RubisCO and exclude O2, suppressing its wasteful oxygenase reaction.",
        "w": [
            "To harvest light energy in deep, low-light environments.",
            "To store excess ATP and NADPH generated during the light reactions.",
            "To physically separate the nitrogenase enzyme from oxygen."
        ],
        "type": "normal",
        "module": "M08"
    },
    {
        "q": "Why does the green sulfur bacterium Chlorobium use the rTCA cycle instead of the Calvin cycle?",
        "c": "Its RC I produces reduced ferredoxin directly, which drives the key rTCA steps cheaply compared to Calvin's high ATP cost.",
        "w": [
            "It lacks the genes for CODH, forcing it to use the rTCA cycle.",
            "The rTCA cycle produces oxygen, which Chlorobium needs for respiration.",
            "rTCA is the only pathway capable of fixing CO2 in the presence of high H2S."
        ],
        "type": "boss",
        "module": "M08"
    },

    # --- MODULE 9: CARBON CYCLING ---
    {
        "q": "Which gene is considered the universal marker for methanogenesis (and AOM), encoding the enzyme that catalyzes the final step?",
        "c": "mcr (methyl-CoM reductase)",
        "w": [
            "pmoA (particulate methane monooxygenase)",
            "nifH (nitrogenase reductase)",
            "amoA (ammonia monooxygenase)"
        ],
        "type": "normal",
        "module": "M09"
    },
    {
        "q": "In acetoclastic methanogenesis (CH3COOH -> CH4 + CO2), what happens to the two carbon atoms in acetate?",
        "c": "The methyl carbon is reduced to CH4; the carboxyl carbon is oxidized to CO2.",
        "w": [
            "Both carbons are reduced to CH4.",
            "Both carbons are oxidized to CO2, and H2 is used to make CH4.",
            "The methyl carbon is oxidized to CO2; the carboxyl carbon is reduced to CH4."
        ],
        "type": "normal",
        "module": "M09"
    },
    {
        "q": "How does Methylomirabilis oxyfera perform aerobic methane oxidation in strictly anoxic environments?",
        "c": "It produces its own intracellular O2 by disproportionating NO into N2 and O2.",
        "w": [
            "It uses an ANME archaeon partner to provide O2.",
            "It uses sulfate as a direct substitute for oxygen in the MMO enzyme.",
            "It extracts oxygen atoms from water using light energy."
        ],
        "type": "boss",
        "module": "M09"
    },

    # --- MODULE 10: NITROGEN CYCLE ---
    {
        "q": "Both DNRA and Denitrification reduce Nitrate (NO3-). What is the critical ecological difference between their outcomes?",
        "c": "Denitrification produces N2 gas (loss of N from ecosystem); DNRA produces NH4+ (retains bioavailable N).",
        "w": [
            "DNRA produces N2 gas; Denitrification produces NH4+.",
            "Denitrification requires oxygen; DNRA is strictly anaerobic.",
            "DNRA produces NO2- (toxic); Denitrification produces N2O (greenhouse gas)."
        ],
        "type": "normal",
        "module": "M10"
    },
    {
        "q": "What unique physical structure does Brocadia use to sequester the highly toxic intermediate hydrazine (N2H4) during anammox?",
        "c": "The anammoxosome",
        "w": [
            "The carboxysome",
            "The chlorosome",
            "The heterocyst"
        ],
        "type": "normal",
        "module": "M10"
    },
    {
        "q": "How does the cyanobacterium Anabaena fix nitrogen despite producing oxygen via photosynthesis (which destroys nitrogenase)?",
        "c": "It differentiates thick-walled heterocysts that lack PS II, creating an anoxic space for nitrogenase.",
        "w": [
            "It secretes a thick layer of protective slime that blocks O2 diffusion.",
            "It only fixes nitrogen at night when photosynthesis is off.",
            "It uses an O2-tolerant variant of nitrogenase bound to ferredoxin."
        ],
        "type": "normal",
        "module": "M10"
    },
    {
        "q": "In the anammox reaction, NO2- serves a dual role. What are these two roles?",
        "c": "Electron acceptor for catabolism (NH4+ oxidation) AND electron donor for anabolism (CO2 fixation via reverse Nxr).",
        "w": [
            "Carbon source for biomass AND nitrogen source for amino acids.",
            "Energy source for phototrophy AND electron acceptor for fermentation.",
            "Electron donor for catabolism AND electron acceptor for anabolism."
        ],
        "type": "boss",
        "module": "M10"
    }
]

with open("questions.json", "w") as f:
    json.dump(questions, f, indent=4)
print("Questions successfully generated and saved to questions.json")
