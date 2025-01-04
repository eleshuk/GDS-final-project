import pandas as pd
import random

# Caminhos dos ficheiros
input_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\StockMarket\MarketData.xlsx"
output_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\StockMarket\MarketData_with_PricePerTon.xlsx"

# Intervalos de preço por cultura (em euros por tonelada)
price_ranges = {
    "almond": (200, 600),
    "apples": (150, 300),
    "apricots": (180, 400),
    "asparagus": (200, 500),
    "avocados": (300, 800),
    "banana": (100, 200),
    "barley": (80, 200),
    "bean": (100, 250),
    "beans__green": (50, 120),
    "blueberries": (500, 1000),
    "broad_beans": (100, 220),
    "broad_beans_and_horse_beans__green": (90, 200),
    "cabbages": (30, 100),
    "carrots_and_turnips": (40, 120),
    "cauliflowers_and_broccoli": (50, 150),
    "cereal": (80, 250),
    "cereals_n_e_c_": (70, 230),
    "cherries": (300, 700),
    "chestnut": (250, 600),
    "chickpeas": (120, 300),
    "chillies_and_peppers__green__capsicum_spp__and_pimenta_spp_": (200, 600),
    "citrus_fruit": (100, 250),
    "cucumbers_and_gherkins": (40, 150),
    "currants": (400, 800),
    "eggplants": (80, 180),
    "fibre_crops__fibre_equivalent": (100, 300),
    "figs": (250, 600),
    "flax__raw_or_retted": (100, 300),
    "fruit": (120, 400),
    "garlic": (200, 600),
    "grapefruit": (80, 200),
    "grapes": (200, 500),
    "groundnut": (150, 350),
    "hazelnuts": (400, 900),
    "hempseed": (100, 300),
    "hop_cones": (400, 800),
    "kiwi": (300, 700),
    "leeks": (40, 120),
    "lemons_and_limes": (100, 250),
    "lettuce": (20, 80),
    "linseed": (100, 250),
    "locust_beans__carobs_": (50, 150),
    "lupins": (70, 180),
    "maize": (80, 200),
    "melon": (80, 200),
    "millet": (60, 150),
    "oats": (60, 150),
    "oilcrops__cake_equivalent": (150, 300),
    "oilcrops__oil_equivalent": (200, 500),
    "olives": (100, 300),
    "onions": (50, 120),
    "onions_and_shallots__green": (40, 100),
    "orange": (100, 250),
    "other_berries_and_fruits_of_the_genus_vaccinium_n_e_c_": (300, 900),
    "other_fruits__n_e_c_": (120, 400),
    "other_nuts__excluding_wild_edible_nuts_and_groundnuts__in_shell__n_e_c_": (300, 700),
    "other_pome_fruits": (150, 350),
    "other_pulses_n_e_c_": (80, 200),
    "other_stone_fruits": (200, 500),
    "other_vegetables__fresh_n_e_c_": (30, 100),
    "peaches_and_nectarines": (200, 500),
    "pears": (140, 280),
    "peas__green": (40, 120),
    "pineapples": (200, 500),
    "plums": (200, 500),
    "potato": (60, 120),
    "pulses": (70, 200),
    "pumpkins__squash_and_gourds": (30, 90),
    "quinces": (120, 300),
    "raspberries": (500, 1000),
    "rice": (80, 200),
    "roots_and_tubers": (50, 150),
    "rye": (70, 150),
    "safflower_seed": (100, 300),
    "sour_cherries": (300, 700),
    "spinach": (40, 120),
    "strawberries": (300, 800),
    "sugar_crops": (50, 150),
    "sugarbeet": (40, 120),
    "sugarcane": (30, 100),
    "sunflower": (100, 300),
    "sweet_potatoes": (60, 150),
    "tangerines": (100, 250),
    "tea": (400, 1000),
    "tobacco": (300, 800),
    "tomato": (50, 150),
    "treenuts": (300, 900),
    "triticale": (80, 200),
    "true_hemp__raw_or_retted": (100, 300),
    "vegetables": (50, 150),
    "walnuts": (400, 1000),
    "watermelons": (60, 150),
    "wheat": (80, 200),
    "yams": (60, 150)
}

# Taxa de conversão de Escudo para Euro (antes de 1999)
conversion_rate = 200.482
adjustment_factor = 10  # Fator para corrigir preços históricos

# Função para gerar preço por tonelada
def generate_price_per_ton(crop_name, year):
    crop_name = crop_name.lower()
    if crop_name in price_ranges:
        low, high = price_ranges[crop_name]
        base_price = random.uniform(low, high)
        
        # Ajustar preços históricos
        if year < 1999:
            base_price /= conversion_rate
            base_price *= adjustment_factor
        
        return round(base_price, 2)
    else:
        # Preço padrão se a cultura não estiver especificada
        return round(random.uniform(50, 300), 2)

# Carregar o ficheiro de entrada
df = pd.read_excel(input_file)

# Gerar dados para PricePerTon
df["PricePerTon"] = df.apply(lambda row: generate_price_per_ton(row["CropName"], row["Year"]), axis=1)

# Salvar o ficheiro de saída
df.to_excel(output_file, index=False)

print(f"Dados gerados e salvos em: {output_file}")
