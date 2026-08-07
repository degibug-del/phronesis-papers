# Energy Harvesting Systems

*by Diego Rincón · phronesis.world*

**Every vibrating thing near you is a small, honest power source. This course teaches you to read it, rate it, and harvest it — and shows why the same math that governs a mass on a spring governs every system you hold away from rest.**

## Who this is for

You build things. Sensors, wearables, small robots, instruments that have to live somewhere a power cord can't reach. Or you don't build yet, but you want to — and you keep seeing claims about shoes that charge phones and floors that power cities, and something in you suspects the numbers don't close.

This course gives you two things. First, the actual physics of mechanical energy harvesting, at the scale where it's real: microwatts to a few watts, sensors and implants, not phones and houses. Second, a framework — ground state, displacement, the cost of staying away, the price of going back — that you'll use on every system you ever design, including the one you live inside.

No prerequisites beyond arithmetic and curiosity. Every number in here is either an order of magnitude from physics or a toy model clearly labeled as one. Nothing is inflated, because inflated numbers are how harvesting projects die.

## Module 1: The Mass at Rest

### S0 is a physical place

Hang a mass on a spring and let it settle. It finds the point where spring force balances gravity, and it stays there forever, asking nothing. That point is the ground state, S0: the configuration the system is built to occupy when nothing pushes on it. Not a metaphor here. You can mark it with a pencil.

Everything in this course follows from one observation: a system sitting at S0 produces nothing. Zero displacement, zero stored energy, zero flow. Rest is cheap, and rest is sterile.

If you want power out of a system, you must first put it somewhere it doesn't want to be.

### Displacement is stored potential

Pull the mass down. Call where it actually is the actual state, S*, and call the gap between actual and ground the displacement: xi = S* − S0. The spring now stores energy, and the energy grows fast with the gap — for an ideal spring, with the square of it. Double the displacement, four times the stored energy.

The gap is the battery. No gap, no energy. This is the displacement framework in its native habitat, the place where none of it can be fudged: displacement is distance, cost is heat, return is motion you can watch.

There are two readings of displacement, and the whole craft of harvesting lives in the difference. Displacement you didn't choose and don't collect on is a liability — stress in a bracket, slop in a bearing, a load held at arm's length for no reason. Displacement you chose, sized, and collect on is an asset. A harvester is the second reading, engineered on purpose.

### D(xi): the cost of staying away

Hold the mass displaced and, in the ideal spring, nothing decays. Real systems are not ideal. The moment anything moves — and in a harvester, things move constantly — the system pays rent: air drag, friction in joints, hysteresis inside the material, eddy currents in nearby metal. Call the rate of that rent D(xi): the cost per unit time of operating away from ground. In most mechanical systems it's paid in proportion to how fast you're moving, so an oscillator pays it on every single pass, going out and coming home.

Here is the reframe that makes you a harvester instead of a victim: D is not the enemy. D is the toll booth. Energy leaving the oscillation is going to exit through damping no matter what. The only question is who collects — friction, which turns it into useless heat, or your transducer, which turns it into charge on a capacitor. Harvesting is the art of standing at the toll booth.

### The strange generosity of springs

In the general framework, going back to ground costs something. C_return is the one-time price of the trip home: the cleanup, the apology, the refactor, the move. You weigh it against the daily rent D and decide when returning beats staying.

Elastic systems invert this, and the inversion is the deepest idea in the course. Release the displaced mass and the spring pays you to come home — the stored energy comes back as motion, and motion is exactly what a transducer eats. In a good harvester, C_return is negative. The return stroke is the harvest stroke.

So a harvester, described in framework terms, is this: a system deliberately held away from S0, returned to it on a schedule, with a collector positioned to take its cut on every return. Sustained oscillation is not chaos. It is displacement and return, displacement and return, metronomically — a maintenance schedule running at mechanical speed.

Hold that picture. The rest of the course is just learning to run that loop well.

### Practice

This week: find three oscillating or displaced systems within reach — a washing machine mid-cycle, a fan with a wobble, a door on a spring closer, your own knee on a walk. For each, write four lines: where is S0, where is S* right now, what is paying D (name the actual friction), and who collects the toll — nobody, heat, or something useful.

- Which of the three has the largest displacement nobody is collecting on?
- Where in your own week do you pay D on a displacement you never chose?
- Can you name one system you maintain where the return stroke already pays you back?

## Module 2: The Honest Numbers

### What a body actually makes

A walking human runs on a metabolic budget in the rough region of a hundred watts — but that is what the body burns, not what you can take. What you can extract without burdening the walker is a small slice of the motion that would otherwise be wasted: the heel strike, the swing of the knee, the bounce of a loaded backpack.

The honest ranges, from decades of published devices, are these. Heel-strike piezoelectric inserts: milliwatts. Electromagnetic knee and backpack harvesters, the bulky kind you notice wearing: from tens of milliwatts up to a few watts at the very top, and the top end costs the wearer real effort. A swinging-mass wrist generator, the mechanism inside an automatic watch: on the order of microwatts. Machine vibration collected by a tuned mass bolted to a motor housing: typically milliwatts. Body-heat thermoelectric patches: microwatts to low milliwatts.

Those are orders of magnitude, not promises. Your build lands wherever your source and your damping budget put it. But the ceiling is physics, not engineering pessimism: harvestable power scales with the moving mass and with the square of the source acceleration, and a wearable's mass must be small and its comfortable acceleration is small. You cannot lever your way past that with cleverness. You can only stop wasting what's there.

### The toy arithmetic of charging a phone

Run the model that ends the most common fantasy. As a toy model: suppose your harvester nets a steady one hundred milliwatts while you walk — generous for anything you'd actually wear without complaint. Suppose a phone battery stores on the order of ten watt-hours. Ten watt-hours divided by a tenth of a watt is a hundred hours of continuous walking for one charge, before conversion losses make it worse.

Nobody walks a hundred hours a week. The phone-charging shoe is not an engineering problem awaiting a breakthrough; it is an arithmetic problem that has already been answered. Any pitch, product, or daydream that ignores this answer is selling displacement from reality.

### What milliwatts are actually good for

Now flip the ledger, because milliwatts are not nothing — they are a different and beautiful niche.

A sensor node that sleeps almost all the time, wakes once a minute, takes a reading, transmits a few bytes, and sleeps again has a tiny average draw. Duty cycling — bursts of activity over long rest — is how small harvests power real work. A pacemaker-class implant runs on a microwatt-scale budget; a heartbeat-driven harvester is a serious research target precisely because the load is honest about its size. A vibration sensor bolted to a bridge girder or a motor housing, powered by the very vibration it monitors, can run for decades with no battery to swap.

Notice what the harvest actually buys in that last case. Not power — power was always available from a battery. It buys the deletion of a recurring cost: the technician, the ladder, the shutdown, the swap. In framework terms, a battery-powered remote sensor carries a C_return you must pay over and over, on a schedule, forever. A harvester-powered one pays C_return once, at design time, and then the system maintains itself. That is the real product. You are not selling milliwatts. You are selling the absence of ladders.

### The overclaim tax

The harvesting field has been damaged repeatedly by people who skipped the envelope math — crowd-powered floors and wind trees and charging fabrics whose numbers never survived a single multiplication. Every overclaim taxes every honest builder who comes after, because the audience has learned to flinch.

So adopt this as a design constraint, not a virtue: budget first, dream second. Before you sketch a mechanism, write the load's average draw and the source's plausible yield on one line each, and see whether the first is smaller than the second. If it isn't, no transducer will save you. If it is, you have a project.

### Practice

This week: pick one battery-powered device you own. From its battery capacity and how long it lasts, do the toy division to estimate its average draw. Then look around its actual location and ask: what motion, vibration, or heat within one meter could plausibly cover that draw? Write down the honest answer, even if — especially if — the answer is "nothing."

- Which device in your life has the smallest appetite, and did its smallness surprise you?
- Where have you seen an overclaim — in tech, in self-help, in your own plans — that one multiplication would have ended?
- What recurring C_return in your own systems (the repeated swap, the repeated cleanup) would you pay most to delete?

## Module 3: The Three Levers

### The damping budget

Everything that drains an oscillator drains it through damping. Split the total into two channels: parasitic damping — friction, drag, hysteresis, all the tolls collected by heat — and electrical damping, the drag your transducer deliberately applies, which is the harvest. Energy out of the oscillation divides between these two channels in proportion to their strength.

At resonance — and we'll earn that word properly below — the force you put in does work against damping and nothing else; the spring and the mass trade energy back and forth between themselves for free. So the entire input flows into the damping budget, and your harvest is whatever fraction of that budget your transducer's channel claims. A classic result of the standard model says output power to the load peaks when the electrical damping is matched to the parasitic damping — collect too gently and you leave energy to friction, clamp too hard and you smother the very oscillation you're feeding on.

Stare at that budget and you'll see there are exactly three things a designer can do. Three levers. There is no fourth.

### Lever one: cut resistance

Shrink the parasitic channel so a larger share of the toll flows to you. This is the unglamorous lever and usually the most profitable one. Replace sliding joints with flexures — thin blades of metal that bend instead of rub, paying almost nothing in friction. Delete rubbing seals. Use pivot or magnetic bearings where a sleeve would scrape. At the smallest scales, package the device in vacuum so air itself stops taxing the motion.

The general lesson transfers everywhere: before you add effort to a struggling system, remove friction from it. Effort fights the loss; design deletes it.

### Lever two: improve the coupling

Make your transducer the dominant collector at the toll booth. A piezoelectric element generates from strain, so it belongs where the strain is largest — at the clamped root of a vibrating beam, not out at the tip where displacement is big but the material barely stretches. A coil harvests from changing magnetic flux, so it belongs in the steepest field gradient you can shape, not merely near the magnet. Engineers compress all this into a coupling coefficient: how strongly the mechanical side talks to the electrical side.

A weakly coupled harvester is a toll booth built on a side road. The traffic — the energy — flows right past it into heat, and no amount of traffic fixes a booth in the wrong place.

### Lever three: tune amplitude and frequency

Match the system's natural frequency to the source's dominant frequency. Drive an oscillator below its natural frequency and your force wastes itself stretching the spring; drive it above and your force wastes itself shoving the mass around; drive it at resonance and force lines up perfectly with velocity, every push lands on a mass already moving the right way, and amplitude — your stored displacement — builds enormously from small, well-timed inputs.

Amplitude is the other half of the lever. Bigger swings store and deliver more energy, but every real device has stroke limits, and hitting the end-stops converts your harvest into noise and fatigue cracks. Tune for the largest swing the hardware tolerates, and not a millimeter more.

### The maintenance theorem, in steel

Now the theorem this whole framework rests on, stated plainly. Maintenance theorem: returning to ground on a schedule beats letting displacement accumulate, and the optimal return frequency balances the fixed cost of each return trip against the cost of accumulated drift. Return too rarely and drift compounds until the trip home is enormous. Return too often and the fixed costs of all those trips eat you alive. Somewhere between is a best frequency.

A resonant harvester is this theorem built out of steel. The oscillator returns to S0 on every cycle — the most disciplined maintenance schedule that exists — and resonance is the optimal return frequency made physical: the one rhythm at which every unit of input effort lands in the budget that includes your harvest, with nothing squandered fighting the spring or the mass.

You already run this theorem, badly or well, on everything you maintain. The inbox, the workshop, the codebase, the friendship. Each has a natural frequency — a return rhythm at which small, regular inputs keep displacement bounded and cheap. Too rare, and you face archaeology instead of tidying. Too frequent, and you spend your week paying setup costs. The skill is the same as the bench skill: find the resonance and drive at it.

### Practice

This week: choose one lossy system — a squeaking machine, a sticking drawer, a recurring task that takes longer than it should — and apply exactly one lever. Cut a friction, improve a coupling (put the collection point where the energy actually is), or change the rhythm at which you return to it. One lever, one week, observe the change.

- In the system you chose, what share of the toll was going to pure heat — effort producing nothing?
- What in your life are you driving off-resonance: pushing at a rhythm the system doesn't want?
- Which return schedule of yours is set by habit rather than by balancing return cost against drift?

## Module 4: Resonance and the Mycelia Principle

### Why the big single harvester loses

A sharply tuned resonator is a bet placed on one frequency. Make the tuning sharper — engineers say higher Q — and the reward at the exact target frequency grows, but the band where the device works at all narrows to a sliver. Real sources do not honor such bets. Motors change speed with load. A walker's gait shifts with terrain and tiredness. A bridge sings differently in summer and winter.

So the lone, perfectly tuned, maximally optimized harvester is fragile in exactly the way every over-optimized system is fragile: superb in the world it was designed for, deaf in the world that actually arrives.

### The mycelia principle

Fungal networks solved this problem long before engineers met it. A mycelium doesn't build one giant root aimed at one predicted nutrient source. It spreads many small threads, each cheap, each slightly different, covering ground, sharing what any thread finds with the whole network.

The harvesting analog is direct and well documented in the literature: instead of one resonator, build an array of small ones, each tuned slightly differently, so the array as a whole covers a band of frequencies rather than a point. When the source drifts, some element of the population is always near resonance. When one element fails, the array dims instead of dying.

The principle repeats one level up, and this is where harvesting earns its keep in the world: the natural product of milliwatt harvesting is not one powerful node but a population of self-sufficient small ones — dozens of sensors scattered through a structure, each sipping from its own local vibration, each modest, the network as a whole seeing everything. Many small, slightly varied, locally fed units beat one large, perfectly tuned, centrally fed unit in any environment that changes. That sentence is about harvesters, organizations, investment portfolios, and skill sets, and it is equally true of all of them.

### Store and burst

Harvest arrives as a trickle; useful work leaves in bursts. Radio transmissions, measurements, and actuations all want brief surges far above the average harvest rate. The reconciliation is storage — usually a supercapacitor — that integrates the trickle for minutes and spends it in milliseconds.

The discipline that makes it work: never schedule a burst bigger than the trickle can refill before the next one. The node's whole life is rhythm — sip, sip, sip, act. Get the rhythm wrong by even a little and the storage walks slowly down to empty; the failure arrives weeks later, far from the mistake. Thin budgets, mechanical or personal, fail exactly this way: not in the moment of overspending, but downstream, after the reserve quietly runs out.

### Reading the source spectrum

Before you tune anything, measure the source. Strap your phone — its accelerometer is a respectable instrument — or a cheap IMU board to the motor, the railing, the floor that interests you. Log a few minutes of vibration during honest operating conditions. Run a frequency analysis (a free app or a dozen lines of code) and find the dominant peaks, their strength, and how they wander over time.

Design to the spectrum you measured, not the one you imagined. This is S0 discipline applied to your own beliefs: the measurement is ground truth, and every assumption you hold instead of it is a displacement you are paying daily rent on without knowing the rate.

### Practice

This week: log a real vibration source for at least a few minutes — a phone accelerometer app on a washing machine, an HVAC unit, a stair rail by a busy walkway. Find the dominant frequency. Then watch whether it stays put across conditions or wanders.

- Did the source behave as you assumed before measuring? Where exactly was your assumption displaced from the data?
- Where in your work are you the single sharply tuned resonator — superb at one frequency, deaf to drift?
- What trickle in your life could feed a burst, if only you added storage between them?

## Module 5: The Build

### Characterize before you design

The order of operations, and it is an order, not a menu:

First, the source: measured spectrum, dominant frequency, acceleration level, and how both drift. Second, the load: average draw and burst profile of the thing you intend to power, in real numbers from its datasheet or your own measurement. Third, the feasibility line: source yield versus load appetite, the Module 2 arithmetic, performed before any metal is cut. Fourth, transduction choice. Fifth, resonator design — mass, stiffness, and damping chosen so the natural frequency sits on the measured peak. Sixth, storage and power electronics. Seventh, the honest test.

Most failed harvesting projects ran this list backwards: fell in love with a transducer, then went looking for a source and a story.

### Choose your transduction

Three mature options, chosen by the source's frequency and amplitude, never by fashion.

Piezoelectric: a crystal or ceramic that generates charge when strained. Suits higher frequencies and small amplitudes — the buzz of machinery. High voltage, tiny current, no moving parts beyond the flexing element itself, but brittle, and it dislikes large deflections. Electromagnetic: a magnet and coil in relative motion. Suits lower frequencies and larger strokes — human gait, ocean swell, a swaying structure. Low voltage, more current, robust, but bulkier, and it shrinks badly: at millimeter scales the physics turns against coils. Electrostatic: variable capacitors, practical mainly at MEMS scale and needing a priming voltage to start. The experimental fourth, triboelectric — contact electrification, materials tapping and sliding — shows promise for irregular, slappy motions, but treat published figures with the skepticism Module 2 taught you.

Rule of thumb worth memorizing: fast and small favors piezo; slow and large favors magnets.

### Close the loop

Raw transducer output is ragged alternating current; your load wants clean, steady, direct. Between them sit a rectifier, a storage element, and a regulator — and two traps.

The cold-start trap: a dead-flat system must somehow bootstrap, because the smart power-management chip that would harvest efficiently itself needs power to begin. Good harvesting circuits are designed to wake from zero on raw, ugly input. Plan for the dead state on day one.

The measurement trap: open-circuit voltage is the resume; net power delivered into the real load, after every conversion stage, is the reference check. Piezo elements in particular flatter you with impressive volts at vanishing current. Report — to others and to yourself — only the net number at the load, or you are running an overclaim with extra steps.

### Debug by the framework

When the build disappoints, the framework is the diagnostic tree.

No output at all: is there displacement? Check whether the source is actually moving your mass — mistuning can leave a working mechanism standing nearly still in a vibrating world. Output, but weak: who is collecting the toll? Either parasitic damping is eating the budget (lever one) or your transducer is coupled to the wrong place (lever two). Output that collapses when you drive harder: you've hit stroke limits and the end-stops are taxing you (lever three — back off amplitude or redesign travel). Worked on the bench, died in the field: the source spectrum drifted off your tuning point. Re-measure, then reach for the mycelia principle — broaden, or multiply.

Four failures, four framework questions. You will use the same four on systems with no springs in them at all.

### Practice

This week: specify — or build, if you have parts — the smallest complete harvest loop you can: one source you measured, one transducer element, a rectifier, a supercapacitor, and one honest act of work: a single LED blink, one sensor reading, one transmitted byte. Smallest possible loop, fully closed. A closed tiny loop teaches more than an open grand design.

- Where in your loop is the biggest gap between gross harvest and net delivered work?
- Which step of the order of operations were you most tempted to skip, and what does that temptation tell you?
- What is the smallest fully closed loop in your larger life — something that runs entirely on what it gathers?

## The Worksheet: Your Displacement Ledger

The framework only pays if you run it on your own systems. Fill this table now — first for the harvester or hardware project in front of you, then for at least two systems that have nothing to do with electronics. Be concrete in the cost columns: minutes per day, watts, errors per week, conversations avoided. Vague costs cannot be compared, and the whole point is comparison.

Your decision column takes one of three values. **Hold**: the displacement is deliberate and something is collecting on it — leave it alone. **Return**: the daily cost D now exceeds the amortized cost of going back — schedule the trip home this week. **Re-tune**: the displacement recurs, so the fix isn't one return but a better return frequency — change the schedule, not the state.

| System | S0 — aligned state | S* — actual state | xi — the gap | D(xi) — daily cost | C_return — cost to return | Decision |
|---|---|---|---|---|---|---|
| *Example: bench harvester* | *Tuned to the measured source peak* | *Tuned to the frequency I assumed last month* | *Resonator off the real peak* | *Most of the toll going to heat; weak harvest every day it runs* | *One afternoon: re-measure, re-tune* | *Return* |
| *Example: workshop* | *Every tool findable in under a minute* | *Three projects' parts strewn across the bench* | *No flat surface, no fast starts* | *Minutes lost per session, plus the projects I don't start* | *One focused hour* | *Re-tune: end-of-session reset, small and frequent* |
| Your current build | | | | | | |
| Your workspace | | | | | | |
| Your tools / code / firmware | | | | | | |
| Your daily energy | | | | | | |
| One relationship or commitment | | | | | | |

When you finish, look down the D column and find the largest number nobody is collecting on. That row is your next project, whatever the System column says.

## The Path

A mass at rest produces nothing. A mass yanked violently and randomly produces mostly heat and broken hardware. A mass held deliberately away from ground, returned on a schedule, at the frequency the system itself prefers, with a collector standing at the toll booth — that mass powers a sensor for decades on vibration nobody else noticed.

That is the whole teaching, and it is a daily practice, not a fact you now possess. Each morning, pick one system — the build on the bench, the inbox, your own body at the end of the day — and ask the four questions: Where is S0? Where is S*? Who is collecting the toll on the gap? And is my return frequency chosen, or merely inherited?

Then make one return, on schedule, and let the return stroke pay you.

The frameworks continue at phronesis.world.
