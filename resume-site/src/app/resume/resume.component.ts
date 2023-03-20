import { Component, OnInit } from '@angular/core';

import { ResIt } from '../res-it';
import { ResItService } from '../res-it.service';

@Component({
  selector: 'app-resume',
  templateUrl: './resume.component.html',
  styleUrls: ['./resume.component.css']
})
export class ResumeComponent implements OnInit {
	jobs: ResIt[] = [];
	edus: ResIt[] = [];

	constructor(private resItService: ResItService) {}

	ngOnInit(): void {
		this.getResIts();
	}

	getResIts(): void {
		this.resItService.getItems().subscribe(items => {
			this.jobs = items.filter(item => item.type == "job");
			this.edus = items.filter(item => item.type == "edu");
		});
	}
}
