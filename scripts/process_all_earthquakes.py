#!/usr/bin/env python3
"""
Process and clean all CWA earthquake data (1990-2026).
- Combines 1990-2025 historical catalog (E-A0073-002)
- Appends 2026 active reports from REST API (E-A0015-001 & E-A0016-001)
- Outputs consolidated CSV and year-by-year summary report
"""

import os
import glob
import csv
import json
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

API_KEY = "CWA-B088F5F8-F91F-49DA-A652-28F20EB9960E"
DATA_DIR = "earthquake_data"
RAW_XML_DIR = os.path.join(DATA_DIR, "raw_xml")
OUTPUT_CSV = os.path.join(DATA_DIR, "taiwan_earthquakes_1990_2026.csv")
SUMMARY_JSON = os.path.join(DATA_DIR, "earthquake_yearly_summary.json")

ns = {"cwa": "urn:cwa:gov:tw:cwacommon:0.1"}

def parse_xml_catalogs():
    xml_files = sorted(glob.glob(os.path.join(RAW_XML_DIR, "CWA-EQ-Catalog-*.xml")))
    print(f"Parsing {len(xml_files)} catalog XML files...")
    
    records = []
    
    for file_path in xml_files:
        filename = os.path.basename(file_path)
        year_str = filename.replace("CWA-EQ-Catalog-", "").replace(".xml", "")
        
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            eq_nodes = root.findall(".//cwa:EarthquakeInfo", ns)
            for eq in eq_nodes:
                def get_val(tag):
                    elem = eq.find(f"cwa:{tag}", ns)
                    return elem.text.strip() if elem is not None and elem.text else ""
                
                mag_str = get_val("LocalMagnitude")
                depth_str = get_val("FocalDepth")
                lon_str = get_val("EpicenterLongitude")
                lat_str = get_val("EpicenterLatitude")
                
                try:
                    mag = float(mag_str) if mag_str else None
                except ValueError:
                    mag = None
                    
                try:
                    depth = float(depth_str) if depth_str else None
                except ValueError:
                    depth = None
                    
                try:
                    lon = float(lon_str) if lon_str else None
                except ValueError:
                    lon = None
                    
                try:
                    lat = float(lat_str) if lat_str else None
                except ValueError:
                    lat = None
                
                records.append({
                    "year": int(year_str),
                    "origin_time": get_val("OriginTime"),
                    "longitude": lon,
                    "latitude": lat,
                    "depth_km": depth,
                    "magnitude": mag,
                    "station_number": get_val("StationNumber"),
                    "phase_number": get_val("PhaseNumber"),
                    "min_distance_km": get_val("MinimumEpicenterDistance"),
                    "gap": get_val("gap"),
                    "rms": get_val("rms"),
                    "erh": get_val("erh"),
                    "erz": get_val("erz"),
                    "quality": get_val("Quality"),
                    "source": f"E-A0073-002-{year_str}"
                })
        except Exception as e:
            print(f"Error parsing {filename}: {e}")
            
    print(f"Extracted {len(records)} records from historical XML files.")
    return records

def fetch_2026_rest_api():
    print("Fetching 2026 recent reports from E-A0015-001 (顯著有感) and E-A0016-001 (小區域)...")
    records = []
    
    # 1. E-A0015-001
    try:
        url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0015-001"
        res = requests.get(url, params={"Authorization": API_KEY, "limit": 500, "format": "JSON"})
        if res.status_code == 200:
            data = res.json()
            for item in data.get("records", {}).get("Earthquake", []):
                info = item.get("EarthquakeInfo", {})
                epi = info.get("Epicenter", {})
                mag_val = info.get("EarthquakeMagnitude", {}).get("MagnitudeValue")
                depth_val = info.get("FocalDepth")
                time_str = info.get("OriginTime", "")
                
                year = 2026
                if time_str:
                    try:
                        year = int(time_str[:4])
                    except:
                        pass
                
                records.append({
                    "year": year,
                    "origin_time": time_str,
                    "longitude": epi.get("EpicenterLongitude"),
                    "latitude": epi.get("EpicenterLatitude"),
                    "depth_km": depth_val,
                    "magnitude": mag_val,
                    "station_number": "",
                    "phase_number": "",
                    "min_distance_km": "",
                    "gap": "",
                    "rms": "",
                    "erh": "",
                    "erz": "",
                    "quality": "",
                    "source": "E-A0015-001 (顯著有感)"
                })
    except Exception as e:
        print(f"Error fetching E-A0015-001: {e}")

    # 2. E-A0016-001
    try:
        url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0016-001"
        res = requests.get(url, params={"Authorization": API_KEY, "limit": 500, "format": "JSON"})
        if res.status_code == 200:
            data = res.json()
            for item in data.get("records", {}).get("Earthquake", []):
                info = item.get("EarthquakeInfo", {})
                epi = info.get("Epicenter", {})
                mag_val = info.get("EarthquakeMagnitude", {}).get("MagnitudeValue")
                depth_val = info.get("FocalDepth")
                time_str = info.get("OriginTime", "")
                
                year = 2026
                if time_str:
                    try:
                        year = int(time_str[:4])
                    except:
                        pass
                
                records.append({
                    "year": year,
                    "origin_time": time_str,
                    "longitude": epi.get("EpicenterLongitude"),
                    "latitude": epi.get("EpicenterLatitude"),
                    "depth_km": depth_val,
                    "magnitude": mag_val,
                    "station_number": "",
                    "phase_number": "",
                    "min_distance_km": "",
                    "gap": "",
                    "rms": "",
                    "erh": "",
                    "erz": "",
                    "quality": "",
                    "source": "E-A0016-001 (小區域)"
                })
    except Exception as e:
        print(f"Error fetching E-A0016-001: {e}")
        
    print(f"Fetched {len(records)} active reports from REST API.")
    return records

def main():
    records = parse_xml_catalogs()
    recent_records = fetch_2026_rest_api()
    all_records = records + recent_records
    
    # Write CSV
    fieldnames = [
        "year", "origin_time", "longitude", "latitude", "depth_km",
        "magnitude", "station_number", "phase_number", "min_distance_km",
        "gap", "rms", "erh", "erz", "quality", "source"
    ]
    
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in all_records:
            writer.writerow(r)
            
    print(f"Saved {len(all_records)} total earthquake records to {OUTPUT_CSV}")
    
    # Generate yearly summary
    yearly_stats = {}
    for r in all_records:
        y = r["year"]
        if y not in yearly_stats:
            yearly_stats[y] = {
                "count": 0,
                "magnitudes": [],
                "depths": [],
                "max_mag": 0.0,
                "max_mag_time": "",
                "mag_gte_6": 0,
                "mag_gte_5": 0,
                "mag_gte_4": 0,
            }
        
        stat = yearly_stats[y]
        stat["count"] += 1
        
        m = r["magnitude"]
        if m is not None:
            stat["magnitudes"].append(m)
            if m >= 6.0:
                stat["mag_gte_6"] += 1
            if m >= 5.0:
                stat["mag_gte_5"] += 1
            if m >= 4.0:
                stat["mag_gte_4"] += 1
            if m > stat["max_mag"]:
                stat["max_mag"] = m
                stat["max_mag_time"] = r["origin_time"]
                
        d = r["depth_km"]
        if d is not None:
            stat["depths"].append(d)

    summary_list = []
    for y in sorted(yearly_stats.keys()):
        stat = yearly_stats[y]
        mags = stat["magnitudes"]
        depths = stat["depths"]
        
        avg_mag = round(sum(mags) / len(mags), 2) if mags else 0.0
        avg_depth = round(sum(depths) / len(depths), 1) if depths else 0.0
        min_mag = min(mags) if mags else 0.0
        
        summary_list.append({
            "year": y,
            "total_count": stat["count"],
            "max_magnitude": stat["max_mag"],
            "max_magnitude_time": stat["max_mag_time"],
            "min_magnitude": min_mag,
            "avg_magnitude": avg_mag,
            "avg_depth_km": avg_depth,
            "mag_gte_6": stat["mag_gte_6"],
            "mag_gte_5": stat["mag_gte_5"],
            "mag_gte_4": stat["mag_gte_4"],
        })
        
    with open(SUMMARY_JSON, "w", encoding="utf-8") as f:
        json.dump(summary_list, f, ensure_ascii=False, indent=2)
        
    print(f"Saved yearly summary to {SUMMARY_JSON}")
    
    # Print console preview
    print("\n=== 地震資料年份摘要 (Yearly Summary) ===")
    print(f"{'年份':<6} | {'總次數':<8} | {'最大規模':<8} | {'平均規模':<8} | {'平均深度(km)':<12} | {'規模>=6次數':<10} | {'最大地震發生時間'}")
    print("-" * 85)
    for s in summary_list:
        print(f"{s['year']:<6} | {s['total_count']:<8} | {s['max_magnitude']:<8} | {s['avg_magnitude']:<8} | {s['avg_depth_km']:<12} | {s['mag_gte_6']:<10} | {s['max_magnitude_time']}")

if __name__ == "__main__":
    main()
