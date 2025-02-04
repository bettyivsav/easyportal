import psutil
import platform
import subprocess

class EasyPortal:
    def __init__(self):
        self.system = platform.system()
        if self.system != "Windows":
            raise EnvironmentError("EasyPortal is designed to run on Windows systems only.")

    def get_disk_info(self):
        disk_info = []
        partitions = psutil.disk_partitions()
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append({
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "fstype": partition.fstype,
                "total": usage.total,
                "used": usage.used,
                "free": usage.free,
                "percent": usage.percent
            })
        return disk_info

    def check_disk_health(self):
        health_status = {}
        try:
            result = subprocess.run(["wmic", "diskdrive", "get", "status"], capture_output=True, text=True)
            lines = result.stdout.splitlines()
            for line in lines[1:]:
                if line.strip():
                    status = line.strip()
                    health_status[status] = health_status.get(status, 0) + 1
        except Exception as e:
            health_status = {"Error": str(e)}
        return health_status

    def maintenance_recommendations(self, disk_info):
        recommendations = []
        for info in disk_info:
            if info['percent'] > 80:
                recommendations.append(f"Drive {info['device']} is over 80% full. Consider cleaning up files.")
            if info['fstype'].lower() == 'ntfs':
                recommendations.append(f"Drive {info['device']} is NTFS. Consider defragmentation for better performance.")
        return recommendations

    def run_analysis(self):
        disk_info = self.get_disk_info()
        health_status = self.check_disk_health()
        recommendations = self.maintenance_recommendations(disk_info)

        print("Disk Information:")
        for info in disk_info:
            print(info)

        print("\nDisk Health Status:")
        for status, count in health_status.items():
            print(f"{status}: {count}")

        print("\nMaintenance Recommendations:")
        for recommendation in recommendations:
            print(recommendation)

if __name__ == "__main__":
    portal = EasyPortal()
    portal.run_analysis()