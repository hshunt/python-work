class Dimension_weight():
    dw_d = {}
    
    def __init__(self, dry_wt="", wet_wt="", tank_capa="", seat_ht="", wheelbase="", rake="", 
    trail="", width_hndlbr="", ht_wo_mirror="",):
        self.dry_wt = dry_wt
        self.wet_wt = wet_wt
        self.tank_capa = tank_capa
        self.seat_ht = seat_ht
        self.wheelbase = wheelbase
        self.rake = rake
        self.trail = trail
        self.width_hndlbr = width_hndlbr
        self.ht_wo_mirror = ht_wo_mirror

        self.dw_d = {
            "dry weight":dry_wt,
            "wet weight":wet_wt,
            "tank capacity":tank_capa,
            "seat height":seat_ht,
            "wheelbase":wheelbase,
            "rake":rake,
            "trail":trail,
            "width handlebars":width_hndlbr,
            "height without mirror":ht_wo_mirror,
        }

class Chassis():
    c_d = {}

    def __init__(self, frame="", swingarm="", f_wheel="", r_wheel="", f_tire="",
     r_tire="", f_sus="", r_sus="", f_brk="", r_brk="", inst_display=""):

        self.frame = frame
        self.swingarm = swingarm
        self.f_wheel = f_wheel
        self.r_wheel = r_wheel
        self.f_tire = f_tire
        self.r_tire = r_tire
        self.f_sus = f_sus
        self.r_sus = r_sus
        self.f_brk = f_brk
        self.r_brk = r_brk
        self.inst_display = inst_display
        
        self.c_d = {
            "frame":frame,
            "swingarm":swingarm,
            "front wheel":f_wheel,
            "rear wheel":r_wheel,
            "front tire":f_tire,
            "rear tire":r_tire,
            "front suspension":f_sus,
            "rear suspension":r_sus,
            "front brake":f_brk,
            "rear brake":r_brk,
            "instrument diplay":inst_display,
        }

class Engine():
    e_d = {}

    def __init__(self, e_type="", capacity="", bore="", stroke="", compression="", 
    max_power="", max_torque="", system="", exhaust="", final_drive="", clutch="", gearbox=""):

        self.e_type = e_type
        self.capacity = capacity
        self.bore = bore
        self.stroke = stroke
        self.compression = compression
        self.max_power = max_power
        self.max_torque = max_torque
        self.system = system
        self.exhaust = exhaust
        self.final_drive = final_drive
        self.clutch = clutch
        self.gearbox = gearbox

        self.e_d = {
            "type":e_type,
            "capacity":capacity,
            "bore":bore,
            "stroke":stroke,
            "compression":compression,
            "max power":max_power,
            "max torque":max_torque,
            "system":system,
            "exhaust":exhaust,
            "final drive":final_drive,
            "clutch":clutch,
            "gearbox":gearbox
        }

class Motorcycle():

    def __init__(self, brand, model, **details):
        self.brand = brand.title()
        self.model = model.title()
        self.details = details
        
    def stats(self):
        moto_stats = [self.brand.title() + " " + self.model.title()]
        if len(self.details["engine_details"].e_d) > 0:
            moto_stats.append('Engine details:')
            for data, name in self.details["engine_details"].e_d.items():
                moto_stats.append(f'{data} = {self.details["engine_details"].e_d[data]}')
        if len(self.details["chassis_details"].c_d) > 0:
            moto_stats.append('Chassis details:')
            for data, name in self.details["chassis_details"].c_d.items():
                moto_stats.append(f'{data} = {self.details["chassis_details"].c_d[data]}')
        if len(self.details["dw_details"].dw_d) > 0:
            moto_stats.append('Dimension & Weight details:')
            for data, name in self.details["dw_details"].dw_d.items():
                moto_stats.append(f'{data} = {self.details["dw_details"].dw_d[data]}')

        return moto_stats
        
class MotoDB():
    motorcycles = []

    def add(self, *moto_models):
        for moto_model in moto_models:
            self.motorcycles.append(moto_model)

    def delete(self, *moto_models):
        for moto_model in moto_models:
            for self.motorcycle in self.motorcycles:
                if self.motorcycle.model == moto_model.title():
                    self.motorcycles.remove(self.motorcycle)
        
    def search(self, *moto_models, **get_details):
        for self.motorcycle in self.motorcycles:
            for moto_model in moto_models:
                if self.motorcycle.model == moto_model.title():
                    for get in get_details:
                        if get_details[get] == "model":
                            print(self.motorcycle.model)
                        elif get_details[get] == "brand":
                            print(self.motorcycle.brand)
                        elif get_details[get] == "all":
                            print(self.motorcycle.stats())

    # def update_moto(self, *moto_models, **moto_details):
    #     for moto_model in moto_models:
    #         for self.motorcycle in self.motorcycles:
    #             if self.motorcycle.model == moto_model.title():  
    #                 for key in moto_details:
    #                     if key == "displacement":
    #                         self.motorcycle.displacement = moto_details[key]
    #                     elif key == "model":
    #                         self.motorcycle.model = moto_details[key]
    #                     elif key == "brand":
    #                         self.motorcycle.brand = moto_details[key]

    def moto_print(self):
        for self.motorcycle in self.motorcycles:
            print(self.motorcycle.model)
        if len(self.motorcycles) == 0:
            print("You have no motorcycles in the DB!")

db = MotoDB()

scrambler_1200_xe_engine = Engine(
    "Liquid-cooled, 8 valve, SOHC, 270° crank angle parallel-twin",
    "1200cc", 
    "3.84 in (97.6 mm)", 
    "3.15 in (80 mm)", 
    "11.0:1", "89Hp (66.2kW) @7,400rpm",
    "81.1 FT-lbs (110Nm) @ 3,950 rpm", 
    "Multipoint sequential electronic fuel injection",
    "Brushed 2 into 2 exhaust system with brushed high level silencers", 
    "X ring chain",
    "Wet, multi-plate assist clutch",
    "6-speed",
    )

scrambler_1200_xe_chassis = Chassis(
    "Tubular steel with aluminium cradle",
    "Twin-sided, aluminium",
    "Tubeless 36-spoke 21 x 2.15in, aluminium rims",
    "Tubeless 32-spoke 17 x 4.25in, aluminium rims",
    "90/90-21",
    "150/70 R17",
    "Showa 47mm fully adjustable upside down forks, 9.8 in (250mm) travel",
    "Fully adjustable Ohlins twin shocks with piggy back reservoir, 9.8 in (250mm) rear wheel travel",
    "Twin 320mm Brembo discs, Brembo M50 4-piston radial monobloc calipers, ABS",
    "Single 255mm disc, Brembo 2-piston floating caliper, ABS",
    "TFT multi­functional instrument pack with digital speedometer, trip computer, digital tachometer, gear position indicator, fuel gauge, service indicator, clock and rider modes (Rain/Road/Sport/Off-­road/Rider-Customizable)"
)

scrambler_1200_xe_dw = Dimension_weight(
   "456 lbs (207kg)",
   "n/a",
   "4.2 US gal (16l)",
   "34.2 in (870mm)",
   "61.8 in (1570mm)",
   "26.9 º",
   "5.09 in (129.2mm)",
   "35.6 in (905mm)",
   "49.2 in (1250mm)"
)

scrambler_1200_xe=Motorcycle("Triumph", "Scrambler 1200 XE",
    engine_details=scrambler_1200_xe_engine,
    chassis_details=scrambler_1200_xe_chassis,
    dw_details=scrambler_1200_xe_dw,
    )

# bonneville_t100=Motorcycle("Triumph", "Bonneville T100", "900cc")
db.add(scrambler_1200_xe)

print(scrambler_1200_xe.details["dw_details"].dw_d["dry weight"])

#db.search("scrambler 1200 xe", get="all")

